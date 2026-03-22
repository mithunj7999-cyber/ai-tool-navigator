# backend/database.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH  = os.path.join(BASE_DIR, 'users.db')
    app.config['SQLALCHEMY_DATABASE_URI']        = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
