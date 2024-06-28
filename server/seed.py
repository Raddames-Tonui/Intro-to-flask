from faker import Faker
from models import db, Course, Student
from app import app


faker = Faker()

print("Start seeding ....")
def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
   
        for i in range(5):
            student = Student(name=faker.name(), age=faker.random_int(min=18, max=25), email=faker.email())
            db.session.add(student)
            db.session.commit()
        
        for i in range(10):
            course= Course(name=faker.word(), code = faker.random_int(min=1000, max=5999), description=faker.sentence(), student_id=faker.random_int(min=1, max=5))
            db.session.add(course)
            db.session.commit()

        # student1 = Student(name="Mike", age=20, email="mike@gmail.com")
        # db.session.add(student1)
        # db.session.commit()

        # course1 = Course(name="Math", code="MATH101", description="Mathematics 101", student_id=student1.id)
        # db.session.add( course1)
        # db.session.commit()




seed_data()

print("Seeding completed!")