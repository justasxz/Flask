from flask import Flask
from config import Config
from src.extensions import db, migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializuojame extensionus su app objektu
    db.init_app(app)
    migrate.init_app(app, db)

    # Importuojame modelius, kad Flask-Migrate juos aptiktų
    from src import models

    # Registruojame blueprintus
    from src.routes.main import main_bp
    from src.routes.forms import forms_bp
    from src.routes.users import forms_bp as users_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(forms_bp)
    app.register_blueprint(users_bp)

    return app
