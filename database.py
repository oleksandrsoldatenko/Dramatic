from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from extensions import db

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    liked_movies = db.relationship('Liked', backref='user')
    comments = db.relationship('Comment', backref='user')
    def __str__(self):
      return f"User: {self.username}"
    def __repr__(self):
      return f"User: {self.username}"

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
    
class Comment(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    movie_id: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    
