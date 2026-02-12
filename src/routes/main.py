from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    skaiciai = [
        1, 3, 4, 986, 865, 4, 9865, 1, 65, 54, 46156, 1, 56165, 561, 1,
        56, 15, 1, 156, 156, 156, 65, 4, 484, 8948, 9915, 925, 259, 591,
        145, 8, 65, 156,
    ]
    return render_template("index.html", numbers=skaiciai, vardas="Jonas")


@main_bp.route("/apie")
def about():
    return render_template("about.html")
