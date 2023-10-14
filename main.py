from flask import jsonify, request
from models import Users, app, db
import bcrypt


with app.app_context():
    db.create_all()


@app.route('/')
def mainRoute():
    return jsonify({'message': 'Hello, this is a rest API, endpoints and necessary information are below.'})
