from flask import Flask
from datetime import timedelta
from extensions import db, login_manager
from config import Config

def create_app(): 
    from auth import auth
    from main import main
    
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(Config())
    app.register_blueprint(auth)
    app.register_blueprint(main)
    db.init_app(app)

    login_manager.init_app(app)
    
    return app