import os
import json
from dotenv import load_dotenv

from sqlalchemy import Column, String, Integer, create_engine, DateTime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from uuid import uuid4


# load in dotenv 
load_dotenv() 

database_name = os.getenv('DB_name', 'test')
user = os.getenv('DB_user', 'student')
password = os.getenv('DB_password', 'student')
database_host = os.getenv('DB_host', 'localhost:5432')
database_path = "postgresql://{}:{}@{}/{}".format(user, password, database_host, database_name)

db = SQLAlchemy()
migrate = Migrate()

'''
setup the database
binds flask app and SQLAlchemy service
'''

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)


class User(db.Model):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, default=uuid4)
    full_name = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, full_name, username, email, password):
        
        self.full_name = full_name
        self.username = username
        self.email = email
        self.password = password

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def format(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'role': self.role 
        }

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    imageUrl = Column(String)
    phone = Column(String)
    address = Column(String)

    def __init__(self, phone, address, imageUrl = ""):
        self.imageUrl = imageUrl
        self.phone = phone
        self.address = address

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'imageUrl': self.imageUrl,
            'phone': self.phone,
            'address': self.address
        }


class Todo(db.Model):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    date_created = Column(DateTime)
    due_date = Column(DateTime)

    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date
        }
