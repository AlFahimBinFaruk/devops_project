import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(app)

    from flaskr.todo.routes import todo_bp

    app.register_blueprint(todo_bp)
    
    @app.route('/')
    def home():
        return "server running."

    return app


