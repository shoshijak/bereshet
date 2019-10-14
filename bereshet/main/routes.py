"""Defines the Bereshet route functions."""
from flask import render_template, url_for, request, current_app

# from bereshet.main.forms import EditElementForm, CreateElementForm, SearchElementForm
# from bereshet.models.makor import Makor
from bereshet.elements.mechaber import Mechaber

# from bereshet.models.sefer import Sefer
from bereshet.main import bp
from bereshet.elements.routes import create_mechaber


# @bp.before_app_request
# def before_request():
#    """Define what is to be done before app request (TODO)."""
#    pass


@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
def index():
    """Route function for Bereshet's home page."""
    return render_template("index.html", title="Home")


@bp.route("/create", methods=["GET", "POST"])
def create():
    """Route function for creation of elements to add to Bereshet."""
    return create_mechaber()


# @bp.route('/search', methods=['GET', 'POST'])
@bp.route("/search")
def search():
    """Route function for searching for elements of Bereshet."""
    # form = SearchElementForm()
    # if not g.search_form.validate():
    #    return redirect(url_for('main.explore'))
    # return render_template('search.html', title='Search')
    return render_template("todo.html", title="Search")


@bp.route("/explore")
def explore():
    """Route function for exploring elements of Bereshet."""
    page = request.args.get("page", 1, type=int)
    mechabrim = Mechaber.query.paginate(
        page, current_app.config["ELEMENTS_PER_PAGE"], False
    )
    next_url = (
        url_for("main.explore", page=mechabrim.next_num) if mechabrim.has_next else None
    )
    prev_url = (
        url_for("main.explore", page=mechabrim.prev_num) if mechabrim.has_prev else None
    )
    # TODO: show Mekorot and Sefarim as well
    # mekorot = Makor.query.order_by(Makor.last_edited.desc()).paginate(
    #    page, current_app.config["ELEMENTS_PER_PAGE"], False
    # )
    return render_template(
        "explore.html",
        title="Explore",
        mechabrim=mechabrim.items,
        next_url=next_url,
        prev_url=prev_url,
    )


@bp.route("/mechabrim/<mechaberame>")
def mechaber(mechaber_name):
    """Route function for visualizing and exploring Mechabrim."""
    mechaber = Mechaber.query.filter_by(mechaber_name=mechaber_name).first_or_404()
    # page = request.args.get("page", 1, type=int)
    # mekorot = sefer.mekorot.order_by(Makor.ref).paginate(
    #     page, current_app.config["ELEMENTS_PER_PAGE"], False
    # )
    # next_url = (
    #     url_for("main.sefer", sefername=sefer.name(), page=mekorot.next_num)
    #     if mekorot.has_next
    #     else None
    # )
    # prev_url = (
    #     url_for("main.sefer", sefername=sefer.name(), page=mekorot.prev_num)
    #     if mekorot.has_prev
    #     else None
    # )
    # return render_template('elements/mechaber.html', mechaber=mechaber)
    return render_template("todo.html", mechaber=mechaber)


# @bp.route("/sefarim/<sefername>")
# def sefer(sefername):
#     sefer = Sefer.query.filter_by(sefername=sefername).first_or_404()
#     mechaber = Mechaber.query.filter_by(id=sefer.mechaber_id).first_or_404()
#     page = request.args.get("page", 1, type=int)
#     mekorot = sefer.mekorot.order_by(Makor.ref).paginate(
#         page, current_app.config["ELEMENTS_PER_PAGE"], False
#     )
#     next_url = (
#         url_for("main.sefer", sefername=sefer.name(), page=mekorot.next_num)
#         if mekorot.has_next
#         else None
#     )
#     prev_url = (
#         url_for("main.sefer", sefername=sefer.name(), page=mekorot.prev_num)
#         if mekorot.has_prev
#         else None
#     )
#     return render_template(
#         "elements/sefer.html",
#         sefer=sefer,
#         mechaber=mechaber,
#         mekorot=mekorot.items,
#         next_url=next_url,
#         prev_url=prev_url,
#     )
