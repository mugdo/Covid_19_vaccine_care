import mongoengine as db
from Service import user_class, register_class
from flask import Flask
from flask import jsonify, request
from datetime import date, datetime
from bson.json_util import dumps

mongo = db.connect(db="vaccinCare", host = "localhost", port = 27017)

app = Flask(__name__)
@app.route('/register',methods= ['POST'])
def add_user():
    _json = request.json
    nid = _json['nid']
    center = _json['center']
    date = _json['date']
    users = register_class.Register.objects(reg_date=date).first()
    print("user_info :",users)
    count =0
    if users:
        for user in users:
                count +=1
        print("count = ", count)
        if count>=5:
             return jsonify("This date is full, Please request another time")
    
    if nid and center and date and request.method == 'POST':
        user_value = user_class.User.objects(nid = nid ).first()
        if user_value:
            register_value = register_class.Register.objects(nid = nid ).first()
            if not register_value :
                     id = mongo.db.reg.insert({'id':nid, 'center':center, 'date': date})
                     print("id=",type(nid))
                     reg =register_class.Register(
                             nid =nid,
                             center = center,
                             reg_date= date
                     )
                     reg.save()
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

user = user_class.User(
        nid ="2910",
        name="lisu",
        father="alku",
        mother = "isbul",
        blood_group = "k+",
        address = "ankara")      
# user.save()
    