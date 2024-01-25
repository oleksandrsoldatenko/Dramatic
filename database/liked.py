from flask_login import UserMixin
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.extensions import db

class Liked(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[str] = mapped_column(String, nullable=False)
    rate: Mapped[float] = mapped_column(Float, nullable=False)
    poster_path: Mapped[str] = mapped_column(String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    def __str__(self):
      return f"Liked movie: {self.title}"
    def __repr__(self):
      return f"Liked movie: {self.title}"