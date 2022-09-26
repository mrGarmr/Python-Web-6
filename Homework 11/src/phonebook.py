
from sqlalchemy import and_
from src import db
from src import models
from src.libs.file_service import move_user_pic, delete_user_pic
# from src.repository.users import find_by_id
from faker import Faker
fake = Faker()


def get_phonebook_user(user_id):
    return db.session.query(models.Contact).filter(models.Contact.user_id == user_id).all()


def get_contact_user(name, user_id):
    return db.session.query(models.Contact).filter(
        and_(models.Contact.user_id == user_id, models.Contact.name == name)).one()


def add_contact(user_id):
    for i in range(10):
        name = fake.first_name()
        phone = fake.phone_number()
        email = fake.ascii_free_email()
        notes = 'FAKE'

        contact = models.Contact(name=name, phone=phone, email=email, notes=notes, user_id=user_id)
        db.session.add(contact)
        db.session.commit()

#
# def update_picture(pic_id, user_id, description):
#     picture = get_picture_user(pic_id, user_id)
#     picture.description = description
#     db.session.commit()
#
#
# def delete_picture(pic_id, user_id):
#     picture = get_picture_user(pic_id, user_id)
#     db.session.query(models.Picture).filter(
#         and_(models.Picture.user_id == user_id, models.Picture.id == pic_id)).delete()
#     delete_user_pic(picture.path)
#     db.session.commit()
#
# add_contact('1')
# add_contact('2')