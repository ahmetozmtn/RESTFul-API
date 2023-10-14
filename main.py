from flask import jsonify, request
from models import Users, app, db
import bcrypt


with app.app_context():
    db.create_all()


@app.route('/')
def mainRoute():
    return jsonify({'message': 'Hello, this is a rest API, endpoints and necessary information are below.'})


@app.route('/api/addData', methods=['POST'])
def addData():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        email = request.json.get('email')
        phone = request.json.get('phone')
        address = request.json.get('address')
        city = request.json.get('city')
        state = request.json.get('state')
        product_name = request.json.get('product_name')
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())
        print(hashed_password)
        newData = Users(username=username, password=hashed_password, email=email,
                        phone=phone, address=address, city=city, state=state, product_name=product_name)
        db.session.add(newData)
        db.session.commit()
        return jsonify({'message': 'the data was successfully added to the database'})
    except Exception as error:
        return jsonify({'message': error})


@app.route('/api/deleteData/<int:id>', methods=['DELETE'])
def deleteData(id):
    try:
        if Users.query.filter_by(id=id).first():
            # id = request.json.get('id')
            data = Users.query.filter_by(id=id).first()
            print(data)
            db.session.delete(data)
            db.session.commit()
            return jsonify({'message': 'the data was successfully deleted from the database'})
        else:
            return jsonify({'message': 'the data does not exist in the database'})
    except Exception as error:
        return jsonify({'message': error})


@app.route('/api/getData', methods=['GET'])
def getData():
    try:
        datas = Users.query.all()
        print(datas)
        datalist = []
        datalist = [{"id": data.id, "username": data.username,
                    "password": data.password.decode('utf-8'), "email": data.email, "phone": data.phone, "address": data.address, "state": data.state, "city": data.city, "product_name": data.product_name} for data in datas]
        return jsonify(datalist)
    except Exception as error:
        return jsonify({'message': error})


@app.route("/api/allDelete", methods=['DELETE'])
def allDelete():
    try:
        db.session.query(Users).delete()
        db.session.commit()
        return jsonify({'message': 'all data was successfully deleted from the database'})
    except Exception as error:
        return jsonify({'message': error})
