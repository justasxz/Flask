# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/") # dekoratorius (/ pagrindinis google.com)
# def home():
#     return "<h1>Sveiki atvyke</h1>"

# @app.route("/apie") 
# def about():
#     return "<h2><b>Mes esame labai puiki Kompanija</b></h2>"

# @app.route("/apie/<company>") 
# def about_company(company):
#     return f"<h2><b>Mes esame labai puiki Kompanija pavadinimu {company}</b></h2>"

# app.run()


# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/") # dekoratorius (/ pagrindinis google.com)
# def home():
#     skaiciai = [1,3,4,986,865,4,9865,1,65,54,46156,1,56165,561,1,56,15,1,156,156,156,65,4,484,8948,9915,925,259,591,145,8,65,156]
#     return render_template("index.html", numbers=skaiciai, vardas="Jonas") # paimti ir atvaizduoti nurodyta html faila

# @app.route("/apie") 
# def about():
#     return render_template("about.html")

# @app.route("/forma", methods=["GET"])  # atvaizduoti forma
# def forma():
#     return render_template("forma.html")

# @app.route("/forma_post", methods=["POST"])  # priimti duomenis is formos
# def forma_post():
#     vardas = request.form["vardas"]
#     return f"<h1>Duomenys gauti jusu vardas {vardas}</h1>"

# @app.route("/getai", methods=["GET"])  # priimti duomenis is formos
# def getai():
#     vardas = request.args.get("vardas", "nepaduotas")
#     amzius = request.args.get("amzius", "nepaduotas")

#     return f"""
#     <h1>Gauti GET parametrai</h1>
#     <p>vardas: {vardas}</p>
#     <p>amzius: {amzius}</p>
#     """



# from flask import Flask, render_template, request, url_for, redirect

# app = Flask(__name__)

# @app.route("/") # dekoratorius (/ pagrindinis google.com)
# def home():
#     skaiciai = [1,3,4,986,865,4,9865,1,65,54,46156,1,56165,561,1,56,15,1,156,156,156,65,4,484,8948,9915,925,259,591,145,8,65,156]
#     return render_template("index.html", numbers=skaiciai, vardas="Jonas") # paimti ir atvaizduoti nurodyta html faila

# @app.route("/apie") 
# def about():
#     return render_template("about.html")

# @app.route("/forma", methods=["GET","POST"])  # atvaizduoti forma
# def forma():
#     if request.method == "POST":
#         vardas = request.form["vardas"]
#         return redirect(url_for("home"))
#     else:
#         return render_template("forma.html")




# if __name__ == "__main__": # Tikrina ar cia yra failas kuris yra paleidziamas ar tik importuojamas
#     # tiesa tik tuo atveju jeigu jis yra paleidziamas kaip pagrindinis, o ne importuojamas
#     app.run(debug=True) # Rodo platesnius klaidu pranesimus su debug=True



from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# 1. Sukuriame bazinę klasę (reikalinga Flask-SQLAlchemy 3.0+)
class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///duomenys.db"

# 2. Inicializuojame db nurodant model_class
db = SQLAlchemy(app, model_class=Base)

# 3. Modernus modelio aprašymas
class User(db.Model):
    __tablename__ = "users"  # Nurodome lentelės pavadinimą
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    vardas: Mapped[str] = mapped_column(db.String(100), nullable=False)


# db.create_all()  # Sukuriame lenteles duomenų bazėje pagal aprašytus modelius
@app.route("/") # dekoratorius (/ pagrindinis google.com)
def home():
    skaiciai = [1,3,4,986,865,4,9865,1,65,54,46156,1,56165,561,1,56,15,1,156,156,156,65,4,484,8948,9915,925,259,591,145,8,65,156]
    return render_template("index.html", numbers=skaiciai, vardas="Jonas") # paimti ir atvaizduoti nurodyta html faila

@app.route("/apie") 
def about():
    return render_template("about.html")

@app.route("/forma", methods=["GET","POST"])  # atvaizduoti forma
def forma():
    if request.method == "POST":
        vardas = request.form["vardas"]

        naujas_vartotojas = User(vardas=vardas)
        db.session.add(naujas_vartotojas)
        db.session.commit()

        return redirect(url_for("home"))
    else:
        return render_template("forma.html")




if __name__ == "__main__": # Tikrina ar cia yra failas kuris yra paleidziamas ar tik importuojamas
    # tiesa tik tuo atveju jeigu jis yra paleidziamas kaip pagrindinis, o ne importuojamas
    with app.app_context():  # Užtikriname, kad esame aplikacijos kontekste
        db.create_all()
    app.run(debug=True) # Rodo platesnius klaidu pranesimus su debug=True

