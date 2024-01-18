
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

login_manager = LoginManager()
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    from database import User   
    return User.query.get(int(user_id))


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
