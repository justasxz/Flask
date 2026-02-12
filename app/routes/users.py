from flask import Blueprint

forms_bp = Blueprint("users", __name__,url_prefix="/users") # susikuriu blueprintą forms, kuris bus naudojamas formų apdorojimui


@forms_bp.route("/list", methods=["GET", "POST"])
def list():
    return f"Vartotojų sąrašas [Jonas, Petras, Ona, ...]"

@forms_bp.route("/add", methods=["GET", "POST"])
def add():
    return f"Čia bus forma naujam vartotojui pridėti"

@forms_bp.route("/delete", methods=["GET", "POST"])
def delete():
    return f"Čia bus forma vartotojui ištrinti"

@forms_bp.route("/update", methods=["GET", "POST"])
def update():
    return f"Čia bus forma vartotojui atnaujinti"