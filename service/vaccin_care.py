from model import User,Register 
from flask import jsonify, request, Blueprint
from datetime import date, datetime
import service.helper_function as Get
import mongoengine as db



mongo =db.connect(db="vaccinCare", host = "localhost", port = 27017)


blueprint = Blueprint('user',__name__,url_prefix="/user")
@blueprint.route('/register',methods= ['POST'])
def add_user():
    _json = request.json
    is_given = Get.verfy_user(_json)
    if not is_given:
        return Get.not_found(jsonify)
    
    date = Get.verfy_user_date(_json)
    users = Register.objects(reg_date=date,center = _json['center'])
    count =Get.user_count(users)

    if count>=2 and date == True:
        new_date = Get.serch_date(_json)
        return jsonify("This date is full or request with another date like : "+new_date)

    else:
        if not date:
            date = Get.serch_date(_json)
        else:
            date = _json['date']
    print("date= ",date)
    if request.method == 'POST':
       return Get.register_user(_json, date, jsonify)

    else:
        return Get.return_err_message(jsonify)
        

@blueprint.route('/getUser',methods= ['GET'])
def get_user():
    _json = request.json
    date = _json['date']
    print("date := ",date)

    users = Get.serch_usr_by_date(date)
    print("Number of user : ",len(users))
    return jsonify(users)




    