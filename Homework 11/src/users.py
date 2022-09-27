from sqlalchemy import and_

from src import db
from src import models
import bcrypt


def create_user(email, password, nickname):

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=10))
    user = models.User(username=nickname, email=email, hash=hashed)
    db.session.add(user)
    db.session.commit()
    return user


def create_contact(name, phone, email, notes, user_id):
    contact = models.Contact(name = name, phone = phone, email = email, notes = notes, user_id = user_id)
    db.session.add(contact)
    db.session.commit()

def login(email, password):
    user = find_by_email(email)
    if not user:
        return None
    if not bcrypt.checkpw(password.encode('utf-8'), user.hash):
        return None
    return user


def find_by_email(email):
    user = db.session.query(models.User).filter(models.User.email == email).first()
    return user


def find_by_id(_id):
    user = db.session.query(models.User).filter(models.User.id == _id).first()
    return user


def delete_contact(name, user_id):
    db.session.query(models.Contact).filter(and_(models.Contact.user_id == user_id, models.Contact.name == name)).delete()
    db.session.commit()
    print('Done')

def find_contact(name, user_id):
    user = db.session.query(models.Contact).filter(and_(models.Contact.user_id == user_id, models.Contact.name == name)).all()
    return user
