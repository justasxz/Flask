from flask import Blueprint, flash, render_template, request, url_for, redirect
from src.extensions import db
from src.models.user import User
from src.forms.auth import LoginForm

forms_bp = Blueprint("forms", __name__) # susikuriu blueprintą forms, kuris bus naudojamas formų apdorojimui


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
