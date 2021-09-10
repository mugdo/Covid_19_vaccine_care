from re import match
from flask import Flask
from flask_pymongo import PyMongo
from flask_pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key ="secretkey"
app.config['MONGO_URI'] = "mongodb://localhost:27017/vaccinCare"

mongo = PyMongo(app)
@app.route('/register',methods= ['POST'])
def add_user():
    _json = request.json
    _id = _json['id']
    _name = _json['full name']
    _phone = _json['phone']
    _center = _json['center']
    _address = _json['address']


    
    if _id and _name and _phone and _center and  request.method == 'POST':
        recived_data= mongo.db.register.find()
        print("data :=", recived_data)
        for data in recived_data:
            for da in data:
                 print(da)
        id = mongo.db.register.insert({'id':_id,'name': _name, 'phone': _phone, 'center':_center, 'address' : _address})
        resp = jsonify("User added succesfully")
        resp.status_code = 200
        return resp
    else:
        return 4004


if __name__ == "__main__":
    app.run(debug=True)