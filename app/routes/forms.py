from flask import Blueprint, flash, render_template, request, url_for, redirect
from app.extensions import db
from app.models.user import User
from app.forms.auth import LoginForm

forms_bp = Blueprint("forms", __name__)


@forms_bp.route("/forma", methods=["GET", "POST"])
def forma():
    try:
        if request.method == "POST":
            vardas = request.form["vardas"]

            naujas_vartotojas = User(vardas=vardas)
            db.session.add(naujas_vartotojas)
            db.session.commit()
            flash("Vartotojas sėkmingai pridėtas!")

            return redirect(url_for("main.home"))
        else:
            form = LoginForm()
            if form.validate_on_submit():
                flash("Formos duomenys sėkmingai patvirtinti!")
                return redirect(url_for("main.home"))
            return render_template("forma.html", form=form)
    except Exception as e:
        flash(f"Įvyko klaida: {e}")
        return redirect(url_for("forms.forma"))
