"""
Defines the errors' API.

Errors are represented in JSON as:

.. code-block:: python

    {
        "error": "short error description",
        "message": "error message (optional)"
    }
"""
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code, message=None):
    """
    Return an error response in JSON format.

    status_code: X
    message: X
    """
    payload = {"error": HTTP_STATUS_CODES.get(status_code, "Unknown error")}
    if message:
        payload["message"] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message):
    """
    Return an error response in JSON format to a bad request.

    The most common error that the API is going to return is going to be the code 400,
    which is the error for "bad request". This is the error that is used when the client
    sends a request that has invalid data in it. To make it even easier to generate this
    error, I'm going to add a dedicated function for it that only requires the long
    descriptive message as an argument.

    message: X
    """
    return error_response(400, message)
