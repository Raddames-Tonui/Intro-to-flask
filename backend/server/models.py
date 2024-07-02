
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
db = SQLAlchemy()
from sqlalchemy.orm import validates

from datetime import datetime

# Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_organizer = db.Column(db.Boolean, nullable=False, default=False)

    events = db.relationship('Event', backref='organizer', lazy=True)
    registrations = db.relationship('Registration', backref='user', lazy=True)

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    organizer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    registrations = db.relationship('Registration', backref='event', lazy=True)

class Registration(db.Model):
    __tablename__ = 'registrations'
    registration_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)

# A user has many events
# An event belongs to an organizer 

# A user has many registrations
# An event has many registrations














# class Student(db.Model, SerializerMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     age = db.Column(db.Integer, nullable=True)
#     email= db.Column(db.String(50), nullable=False)

#     courses = db.relationship('Course', backref='student', lazy=True)
#     # serialize_rules = ('-courses.student',)
#     def to_dict(self):
#         return {
#         "id" : self.id,
#         "name" : self.name,
#         "age" : self.age,
#         "email" : self.email,
#         "courses" : [course.to_dict() for course in self.courses]
#         }
    
#     @validates('email')
#     def validate_email(self,key, email):
#         if "@" not in email:
#             raise ValueError("Invalid email")
#         return email
 


# class Course(db.Model, SerializerMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     code = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.String(50), nullable=False)

#     student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

#     def to_dict(self):

#         return {
#         "id" : self.id   ,
#         "name" : self.name,
#         "code" : self.code,
#         "description" : self.description,
#         "student_id" : self.student_id
        
#         }



# class Student(db.Model, SerializerMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     age = db.Column(db.Integer, nullable=True)
#     email= db.Column(db.String(50), nullable=False)

#     courses = db.relationship('Course', backref='student', lazy=True)
#     # serialize_rules = ('-courses.student',)
#     def to_dict(self):
#         return {
#         "id" : self.id,
#         "name" : self.name,
#         "age" : self.age,
#         "email" : self.email,
#         "courses" : [course.to_dict() for course in self.courses]
#         }
    
#     @validates('email')
#     def validate_email(self,key, email):
#         if "@" not in email:
#             raise ValueError("Invalid email")
#         return email
 


# class Course(db.Model, SerializerMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     code = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.String(50), nullable=False)

#     student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

#     def to_dict(self):

#         return {
#         "id" : self.id   ,
#         "name" : self.name,
#         "code" : self.code,
#         "description" : self.description,
#         "student_id" : self.student_id
        
#         }



