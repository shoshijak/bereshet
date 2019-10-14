"""Defines error handlers."""
from flask import render_template, request
from bereshet import DB
from bereshet.errors import bp
from bereshet.api.errors import error_response as api_error_response


def wants_json_response():
    """
    Determine whether a request wants a JSON response.

    This is a helper function in this module.

    What I want to do is modify the global application error handlers so that they use
    content negotiation to reply in HTML or JSON according to the client preferences.
    This can be done using the request.accept_mimetypes object from Flask:
    The wants_json_response() helper function compares the preference for JSON or HTML
    selected by the client in their list of preferred formats. If JSON rates higher than
    HTML, then I return a JSON response. Otherwise I'll return the original HTML
    responses based on templates. For the JSON responses I'm going to import the
    error_response helper function from the API blueprint, but here I'm going to rename
    it to api_error_response() so that it is clear what it does and where it comes from.
    """
    return (
        request.accept_mimetypes["application/json"]
        >= request.accept_mimetypes["text/html"]
    )


@bp.app_errorhandler(404)
def not_found_error(error):
    """
    Route the 404 'not-found-error'.

    This error occures when ...
    """
    if wants_json_response():
        return api_error_response(404)
    return render_template("errors/404.html"), 404


@bp.app_errorhandler(500)
def internal_error(error):
    """
    Route the 500 'internal error'.

    This error occures when ...
    """
    DB.session.rollback()
    if wants_json_response():
        return api_error_response(500)
    return render_template("errors/500.html"), 500
