# SQLAlchemy operations

# Flask
from flask import Flask, request, jsonify
from flask_migrate import Migrate

app  = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///school.db" # postgres
# Serializer

from models import db, Student, Course
migrate = Migrate(app, db)
db.init_app(app)


@app.route("/v1/students", methods=["GET"])
def fetch_students():
    students = Student.query.all()
    # student_list = []
    # for student in students:
    #     student_list.append({"id": student.id, "name": student.name, "age": student.age, "email": student.email})
    # print(students)

    student_list = [student.to_dict() for student in students]
    return jsonify(student_list), 200



@app.route("/v1/students/<int:id>", methods=["GET"])
def fetch_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict()), 200

@app.route("/v1/students", methods=["POST"])
def add_student():
    data = request.get_json()
    new_student = Student(name=data["name"], age=data["age"], email=data["email"])

    db.session.add(new_student)
    db.session.commit()
    return jsonify({"success":"Student_created successfully!"}), 201

# Update student
@app.route("/v1/students/<int:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()

    student.name = data["name"]
    student.email = data["email"]
    student.age = data["age"]

    db.session.commit()
    return jsonify({"success":"Student updated successfully!"}), 201

# DELETE student
@app.route("/v1/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get_or_404(id)

    student_courses = Course.query.filter_by(student_id=id).all()
    for course in student_courses:
        db.session.delete(course)
        db.session.commit()

    db.session.delete(student)
    db.session.commit()
    return jsonify({"success":"Student deleted successfully!"}), 200

if __name__ == "__main__":
    app.run(debug=True)