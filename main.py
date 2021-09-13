from datetime import date, datetime
from re import match
from flask import Flask
from flask_pymongo import PyMongo
from flask_pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash, check_password_hash
import datetime



app = Flask(__name__)
# app.secret_key ="secretkey"
app.config['MONGO_URI'] = "mongodb://localhost:27017/vaccinCare"

mongo = PyMongo(app)
@app.route('/register',methods= ['POST'])
def add_user():
    _json = request.json
    id = _json['id']
    center = _json['center']
    date = _json['date']
    # d = datetime.datetime.now()
    # _date = d.strftime("%x")
    users = mongo.db.reg.find({ "date": date})
    count =0
    for user in users:
        count +=1
    print("count = ", count)
    if count>=5:
        return jsonify("This date is full, Please request another time")
    
    if id and center and date and request.method == 'POST':
        user_value = mongo.db.users.find_one({ "id no": id })
        if user_value:
            register_value = mongo.db.reg.find_one({ "id": id })
            if not register_value :
                     id = mongo.db.reg.insert({'id':id, 'center':center, 'date': date})
                     resp = jsonify("Registation succesfully")
                     resp.status_code = 200
                     return resp
            else:
                 return jsonify("Alredy Registed")
        else:
            return jsonify("User Not found")
    else:
        resp =jsonify("Not found")
        resp.status_code= 404
        return resp

@app.errorhandler(404)
def not_found(error = None):
    message  = {
        'status': 404,
        'message ': 'You have to give 3 fild'
    }
    resp = jsonify(message)
    resp.status_code= 404
    return resp

@app.route('/getUser',methods= ['GET'])
def get_user():
    _json = request.json
    date = _json['date']
    print("date := ",date)

    users = mongo.db.reg.find({ "date": date})
    resp = dumps(users)
    return resp


if __name__ == "__main__":
    app.run(debug=True)