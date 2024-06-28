
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
db = SQLAlchemy()


class Student(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    email= db.Column(db.String(50), nullable=False)

    courses = db.relationship('Course', backref='student', lazy=True)
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'courses': [course.to_dict() for course in self.courses]
        }
  


class Course(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'description': self.description
        }



