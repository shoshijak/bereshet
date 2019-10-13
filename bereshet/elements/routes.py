from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from bereshet import db
from bereshet.elements import bp
from bereshet.elements.forms import CreateMechaberForm
from bereshet.elements.mechaber import Mechaber


@bp.route("/create_mechaber", methods=["GET", "POST"])
def create_mechaber():
    form = CreateMechaberForm()
    if form.validate_on_submit():
        mechaber = Mechaber(mechabername=form.mechabername.data)
        db.session.add(mechaber)
        db.session.commit()
        flash('Added mechaber "{}"'.format(mechaber))
        return redirect(url_for("main.create"))
    return render_template("create.html", title="Create Mechaber", form=form)
