from service.model import User,Register 
from flask import jsonify, request, Blueprint
from datetime import date, datetime
import mongoengine as db
from flask.views import MethodView
from flask_restful import Resource, Api
from datetime import datetime, timedelta
from service.controler import func_request


def verfy_user(json_value):

    if  json_value.get("nid") and json_value.get("center"):
       return True

    else:
        return True

def verfy_user_date(json_value):

    if  json_value.get("date"):
        return  True

    else:
        return False

def get_date():
    today = datetime.now()
    return today

def user_count(users):
    count =0
    for user in users:
        count +=1
    return count


def serch_date(_json):
    today = datetime.now()
    flag = True
    res = today
    while(flag):
        user= Register.objects(reg_date=res,center = _json['center'])
        if user_count(user) <=2 :
            return  res
            flag = False
            break
        res = (datetime.strptime(today.strftime('%Y-%m-%d'), '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
def not_found(jsonify):
    message  = {
        'status': 500,
        'message ': 'You have to give nid and center fild'
    }
    resp = jsonify(message)
    resp.status_code= 404
    return resp
def register_user(_json, date, jsonify):
    if User.objects(nid = _json['nid'] ).first():
        if not Register.objects(nid = _json['nid'] ).first() :
            reg =Register(nid =_json['nid'],
            center = _json['center'] ,reg_date= date)
            reg.save()
            resp = jsonify("Registation succesfully")
            resp.status_code = 200
            return resp
        else:
            return jsonify("Alredy Registed")
    else:
        return jsonify("User Not found")

def return_err_message(jsonify):
    message  = {
        'status': 404,
        'message ': 'Request not execute'
    }
    resp = jsonify(message)
    resp.status_code= 404
    return resp



def serch_usr_by_date(date):
   user_array = []
   users =Register.objects(reg_date=date)
   for user in users:
       temp = {
           "nid" : user['nid'],
           "center" : user['center'],
           "reg_date" : user['reg_date']
       }
       print(temp)
       user_array.append(temp)
    
   return user_array
      
        




mongo =db.connect(db="vaccinCare", host = "localhost", port = 27017)


user_blueprint = Blueprint('user',__name__,url_prefix="/user")

class user(MethodView):
    def post(self):
        _json = request.json
        is_given =verfy_user(_json)
        if not is_given:
            return not_found(jsonify)
        
        date = verfy_user_date(_json)
        users = Register.objects(reg_date=date,center = _json['center'])
        count =user_count(users)

        if count>=2 and date == True:
            new_date = serch_date(_json)
            return jsonify("This date is full or request with another date like : "+new_date)

        else:
            if not date:
                date = serch_date(_json)
            else:
                date = _json['date']
        print("date= ",date)
        if request.method == 'POST':
            return register_user(_json, date, jsonify)

        else:
            return return_err_message(jsonify)
        
    def get(self):
        _json = request.json
        date = _json['date']
        print("date := ",date)

        users = serch_usr_by_date(date)
        print("Number of user : ",len(users))
        return jsonify(users)
    
func_request(user_blueprint,Api,user)
 




    