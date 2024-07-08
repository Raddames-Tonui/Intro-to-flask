from faker import Faker
from models import db, User, Event, Registration
from app import app, bcrypt


faker = Faker()
from datetime import datetime

print("Start seeding ....")
def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
   
        password =  bcrypt.generate_password_hash('kkkk').decode('utf-8')

        # Users table
        users = [
            User(name='Admin User', email='admin@example.com', password=password, is_admin=True, is_organizer=False),
            User(name='Organizer One', email='organizer1@example.com', password=password, is_admin=False, is_organizer=True),
            User(name='Organizer Two', email='organizer2@example.com', password=password, is_admin=False, is_organizer=True),
            User(name='User One', email='user1@example.com', password=password, is_admin=False, is_organizer=False),
            User(name='User Two', email='user2@example.com', password=password, is_admin=False, is_organizer=False),
            User(name='User Three', email='user3@example.com', password=password, is_admin=False, is_organizer=False)
        ]

        for user in users:
            db.session.add(user)
        
        db.session.commit()

        # Events
        events = [
            Event(event_name='Tech Conference 2024', description='A conference about the latest in tech.', event_date=datetime(2024, 9, 1, 9, 0), location='Tech Hall A', organizer_id=users[1].id),
            Event(event_name='Music Festival', description='A fun music festival with various artists.', event_date=datetime(2024, 10, 15, 17, 0), location='Open Grounds', organizer_id=users[2].id)
        ]

        for event in events:
            db.session.add(event)

        db.session.commit()

        # Registrations
        registrations = [
            Registration(event_id=events[0].id, user_id=users[3].id),
            Registration(event_id=events[0].id, user_id=users[4].id),
            Registration(event_id=events[1].id, user_id=users[5].id)
        ]

        for registration in registrations:
            db.session.add(registration)

        db.session.commit()



seed_data()

print("Seeding completed!")