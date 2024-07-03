# SQLAlchemy operations

# Flask
import random
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from flask_cors import CORS
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()




app  = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///event.db" # postgres
CORS(app)
app.config["SECRET_KEY"] = "jdhfvksdjkgh"+ str(random.randint(1, 1000000))
app.config["JWT_SECRET_KEY"] = "evrfsejhfgvret"+ str(random.randint(1, 1000000))
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
jwt = JWTManager(app)

from models import db, User, Event, Registration
migrate = Migrate(app, db)
db.init_app(app)

from datetime import datetime

# Types of Authentication
# 1. Basic Authentication - Cookies
# 2. JWT Authentication - Tokens - sjgdsrkghugfraekjhsdfgvbsduhkfgeyhlskbvgsjhdfbgvsdjklhlkfvbsdkjfbvsdkjh
        

@app.route("/login", methods=["POST"])
def login_user():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token":access_token})

    else:
        return jsonify({"error": "Wrong credentials"}), 401
    
# Fetch Current user
@app.route("/current_user", methods=["GET"])
@jwt_required()
def current_user():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    user_data = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone_number": user.phone_number,
        "is_admin": user.is_admin,
        "is_organizer": user.is_organizer
    }
    return jsonify(user_data), 200


# Use registration
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    email_exists = User.query.filter_by(email=data['email']).first()
    if email_exists:
        return jsonify({"error": "Email already exists"}), 400
        
    
    new_user = User(
        name=data['name'],
        email=data['email'],
        password= bcrypt.generate_password_hash( data['password'] ).decode('utf-8') ,
        phone_number=data.get('phone_number'),
        is_admin=data.get('is_admin', False),
        is_organizer=True if data['is_organizer']=="true" else False
        # data.get('is_organizer', False)
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"success": "User created successfully"}), 201

# Fetching users requires an user who is an admin
@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    
    if current_user.is_admin:
        users = User.query.all()
        user_list = [{
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone_number": user.phone_number,
            "is_admin": user.is_admin,
            "is_organizer": user.is_organizer
        } for user in users]
        return jsonify(user_list), 200
    else:
        return jsonify({"error": "You are not authorized to view this page"}), 401


@app.route('/users/<int:id>', methods=['GET'])
@jwt_required()
def get_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone_number": user.phone_number,
        "is_admin": user.is_admin,
        "is_organizer": user.is_organizer
    }), 200



#Update Profile should be done the the loggedin user only
@app.route('/users', methods=['PUT'])
@jwt_required()
def update_profile():
    data = request.get_json()

    loggedin_user_id = get_jwt_identity()
    user = User.query.get(loggedin_user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    

    # email_exists = User.query.filter_by(email=data['email']).first()
    # if email_exists:
    #     return jsonify({"error": "Email already exists"}), 400

    user.name = data.get('name', user.name)
    user.email = user.email
    user.password = bcrypt.generate_password_hash( data['password'] ).decode('utf-8') 
    user.phone_number = data.get('phone_number', user.phone_number)
    user.is_admin = data.get('is_admin', user.is_admin)
    user.is_organizer = data.get('is_organizer', user.is_organizer)
    db.session.commit()
    return jsonify({"success": "User updated successfully"}), 200

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200



# CRUD for Event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    new_event = Event(
        event_name=data['event_name'],
        description=data['description'],
        event_date=datetime.strptime(data['event_date'], '%Y-%m-%d %H:%M:%S'),
        location=data['location'],
        organizer_id=data['organizer_id']
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({"message": "Event created successfully"}), 201

@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    event_list = [{
        "id": event.id,
        "event_name": event.event_name,
        "description": event.description,
        "event_date": event.event_date.strftime('%Y-%m-%d %H:%M:%S'),
        "location": event.location,
        "organizer_id": event.organizer_id
    } for event in events]
    return jsonify(event_list), 200

@app.route('/events/<int:id>', methods=['GET'])
def get_event(id):
    event = Event.query.get(id)
    if event is None:
        return jsonify({"message": "Event not found"}), 404
    return jsonify({
        "id": event.id,
        "event_name": event.event_name,
        "description": event.description,
        "event_date": event.event_date.strftime('%Y-%m-%d %H:%M:%S'),
        "location": event.location,
        "organizer_id": event.organizer_id
    }), 200

@app.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    data = request.get_json()
    event = Event.query.get(id)
    if event is None:
        return jsonify({"message": "Event not found"}), 404

    event.event_name = data.get('event_name', event.event_name)
    event.description = data.get('description', event.description)
    event.event_date = datetime.strptime(data.get('event_date', event.event_date.strftime('%Y-%m-%d %H:%M:%S')), '%Y-%m-%d %H:%M:%S')
    event.location = data.get('location', event.location)
    event.organizer_id = data.get('organizer_id', event.organizer_id)
    db.session.commit()
    return jsonify({"message": "Event updated successfully"}), 200

@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.get(id)
    if event is None:
        return jsonify({"message": "Event not found"}), 404

    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event deleted successfully"}), 200

# CRUD for Registration
@app.route('/registrations', methods=['POST'])
def create_registration():
    data = request.get_json()
    new_registration = Registration(
        event_id=data['event_id'],
        user_id=data['user_id']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify({"message": "Registration created successfully"}), 201

@app.route('/registrations', methods=['GET'])
def get_registrations():
    registrations = Registration.query.all()
    registration_list = [{
        "id": registration.id,
        "event_id": registration.event_id,
        "user_id": registration.user_id,
        "registration_date": registration.registration_date.strftime('%Y-%m-%d %H:%M:%S')
    } for registration in registrations]
    return jsonify(registration_list), 200

@app.route('/registrations/<int:id>', methods=['GET'])
def get_registration(id):
    registration = Registration.query.get(id)
    if registration is None:
        return jsonify({"message": "Registration not found"}), 404
    return jsonify({
        "id": registration.id,
        "event_id": registration.event_id,
        "user_id": registration.user_id,
        "registration_date": registration.registration_date.strftime('%Y-%m-%d %H:%M:%S')
    }), 200

@app.route('/registrations/<int:id>', methods=['PUT'])
def update_registration(id):
    data = request.get_json()
    registration = Registration.query.get(id)
    if registration is None:
        return jsonify({"message": "Registration not found"}), 404

    registration.event_id = data.get('event_id', registration.event_id)
    registration.user_id = data.get('user_id', registration.user_id)
    db.session.commit()
    return jsonify({"message": "Registration updated successfully"}), 200

@app.route('/registrations/<int:id>', methods=['DELETE'])
def delete_registration(id):
    registration = Registration.query.get(id)
    if registration is None:
        return jsonify({"message": "Registration not found"}), 404

    db.session.delete(registration)
    db.session.commit()
    return jsonify({"message": "Registration deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)