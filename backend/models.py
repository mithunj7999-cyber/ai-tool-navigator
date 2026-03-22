# backend/models.py
from database import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id         = db.Column(db.Integer, primary_key=True)
    email      = db.Column(db.String(150), unique=True, nullable=False)
    username   = db.Column(db.String(100), nullable=False)
    password   = db.Column(db.String(200), nullable=True)  # None for Google OAuth
    google_id  = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    history    = db.relationship('PromptHistory', backref='user', lazy=True)

class PromptHistory(db.Model):
    __tablename__ = 'prompt_history'
    id         = db.Column(db.Integer, primary_key=True)
    user_id    = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    topic      = db.Column(db.String(500), nullable=False)
    category   = db.Column(db.String(50))
    prompt     = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
