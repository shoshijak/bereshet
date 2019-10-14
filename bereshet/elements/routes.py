"""Defines routes for element-specific functionalities."""

from flask import render_template, redirect, url_for, flash
from bereshet import DB
from bereshet.elements import bp
from bereshet.elements.forms import CreateMechaberForm
from bereshet.elements.mechaber import Mechaber


@bp.route("/create_mechaber", methods=["GET", "POST"])
def create_mechaber():
    """Route the "create_mechaber" functionality."""
    form = CreateMechaberForm()
    if form.validate_on_submit():
        mechaber = Mechaber(mechaber_name=form.mechaber_name.data)
        DB.session.add(mechaber)
        DB.session.commit()
        flash('Added mechaber "{}"'.format(mechaber))
        return redirect(url_for("main.create"))
    return render_template("create.html", title="Create Mechaber", form=form)
