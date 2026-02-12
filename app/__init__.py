from flask import Flask
from config import Config
from app.extensions import db, migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializuojame extensionus su app objektu
    db.init_app(app)
    migrate.init_app(app, db)

    # Importuojame modelius, kad Flask-Migrate juos aptiktų
    from app import models

    # Registruojame blueprintus
    from app.routes.main import main_bp
    from app.routes.forms import forms_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(forms_bp)

    return app
