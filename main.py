import mongoengine as db
from model import user_class, register_class
from flask import Flask
from flask import jsonify, request
from datetime import date, datetime
from bson.json_util import dumps
from Service_Function import service

mongo = db.connect(db="vaccinCare", host = "localhost", port = 27017)

app = Flask(__name__)
@app.route('/register',methods= ['POST'])
def add_user():
    _json = request.json
    is_given = service.verfy_user(_json)
    print()
    if not is_given:
        return service.not_found(jsonify)
    
    date = service.verfy_user_date(_json)
    users = register_class.Register.objects(reg_date=date,center = _json['center'])
    count =service.user_count(users)

    if count>=2 and date == True:
        new_date = service.serch_date(_json)
        return jsonify("This date is full or request with another date like : "+new_date)

    else:
        if not date:
            date = service.serch_date(_json)
        else:
            date = _json['date']
    print("date= ",date)
    if request.method == 'POST':
       return service.register_user(_json, date, jsonify)

    else:
        return service.return_err_message(jsonify)
        

@app.route('/getUser',methods= ['GET'])
def get_user():
    _json = request.json
    date = _json['date']
    print("date := ",date)

    users = service.verfy_user_date(_json)
    return users


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
    