import os
import json
from dotenv import load_dotenv

from sqlalchemy import Column, String, Integer, create_engine, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from uuid import uuid4
from api.utils import generate_hash, check_hash


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
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password_hash = Column(String(200))
    todos = db.relationship('Todo', backref='user')

    def __init__(self, full_name, username, email):
        
        self.full_name = full_name
        self.username = username
        self.email = email

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def set_password(self, password):
        self.password_hash = generate_hash(password) 

    def check_password(self, password): 
        return check_hash(self.password_hash, password)

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
    user = Column(Integer, ForeignKey('user.id'))

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
