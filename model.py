from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(250),unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(250))
    admin = db.Column(db.Boolean)


    def __init__(self,public_id,name,password,admin):
        self.public_id = public_id
        self.name = name
        self.password = password
        self.admin = admin

class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    sex = db.Column(db.String())
    mobile_no = db.Column(db.Integer())
    time = db.Column(db.DateTime, default=datetime.utcnow)
    weight = db.Column(db.Integer())

    def __init__(self,name,age,sex,mobile_no,weight):
        self.name = name
        self.age = age
        self.sex = sex
        self.mobile_no = mobile_no
        self.weight = weight
