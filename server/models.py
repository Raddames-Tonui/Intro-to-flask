
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
db = SQLAlchemy()


class Student(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    email= db.Column(db.String(50), nullable=False)

    courses = db.relationship('Course', backref='student', lazy=True)

    # def to_dict():
    #     pass


class Course(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

# Course
# sandie #2121 jkdhfvksbj 1
# mike #2121 jkdhfvksbj 1# class Enrollment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
#     course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)