import sys, os
sys.path.insert(0, os.path.abspath('..'))
from config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):  # Application Factory

    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    from .models.users import User
    with app.app_context():
        #db.drop_all()
        db.create_all()

    from .main import error, main
    
    app.register_blueprint(error)
    app.register_blueprint(main)

    return app
    
