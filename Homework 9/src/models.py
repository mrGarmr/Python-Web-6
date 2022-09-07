from sqlalchemy import ForeignKey, Column, Integer, Unicode, String
from sqlalchemy.orm import relationship
from src.db import Base, engine


class Contact(Base):
    __tablename__ = 'allcontact'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50), nullable=False)

    # relationship
    phone = relationship('Phone', backref='allcontact',
                         cascade='all, delete, delete-orphan')
    email = relationship('Email', backref='allcontact', cascade='all, delete, delete-orphan')
    note = relationship('Note', backref='allcontact', cascade='all, delete, delete-orphan')
    address = relationship('Address', backref='allcontact', cascade='all, delete, delete-orphan')


class Email(Base):
    __tablename__ = 'email'
    email_id = Column('email_id', Integer, primary_key=True)
    email = Column('email', String(60), nullable=True)

    # relationship
    contact_id = Column(Integer, ForeignKey('allcontact.id', ondelete='CASCADE'), nullable=False)
    contact = relationship('Contact', back_populates='email')


class Note(Base):
    __tablename__ = 'note'
    note_id = Column('note_id', Integer, primary_key=True)
    note = Column('note', String(60), nullable=True)

    # relationship
    contact_id = Column('allcontact', Integer, ForeignKey('allcontact.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    contact = relationship('Contact', back_populates='note')


class Phone(Base):
    __tablename__ = 'phone'
    phone_id = Column('phone_id', Integer, primary_key=True)
    phone = Column('phone', String(10))

    # relationship
    contact_id = Column(Integer, ForeignKey('allcontact.id', ondelete='CASCADE'), nullable=False)
    contact = relationship('Contact', back_populates='phone')

class Address(Base):
    __tablename__ = 'address'
    address_id = Column('address_id', Integer, primary_key=True)
    address = Column('address', String(60), nullable=True)

    # relationship
    contact_id = Column('allcontact', Integer, ForeignKey('allcontact.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    contact = relationship('Contact', back_populates='address')

Base.metadata.create_all(engine)
Base.metadata.bind = engine
