from sqlalchemy.orm import Mapped, mapped_column
from src.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    vardas: Mapped[str] = mapped_column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.id}: {self.vardas}>"
