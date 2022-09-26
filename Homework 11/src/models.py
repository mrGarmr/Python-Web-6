from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from src import db


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    notes = db.Column(db.String(120), unique=True, nullable=True)

    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', cascade='all, delete', back_populates='contacts')

    def __repr__(self):
        return f"Contact ({self.id}, {self.name}, {self.phone})"


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hash = db.Column(db.String(255), nullable=False)
    token_cookie = db.Column(db.String(255), nullable=True, default=None)
    contacts = relationship('Contact', cascade='all, delete', back_populates='user')

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email})"

