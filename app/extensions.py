from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate


class Base(DeclarativeBase):
    pass


# Sukuriame extensionus BE app objekto - tai išvengia circular importų
db = SQLAlchemy(model_class=Base)
migrate = Migrate()
