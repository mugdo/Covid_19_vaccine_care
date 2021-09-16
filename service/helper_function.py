from datetime import datetime, timedelta
from model import user as data
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
        user= data.Register.objects(reg_date=res,center = _json['center'])
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
    if data.User.objects(nid = _json['nid'] ).first():
        if not data.Register.objects(nid = _json['nid'] ).first() :
            reg =data.Register(nid =_json['nid'],
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
   users =data.Register.objects(reg_date=date)
   for user in users:
       temp = {
           "nid" : user['nid'],
           "center" : user['center'],
           "reg_date" : user['reg_date']
       }
       print(temp)
       user_array.append(temp)
    
   return user_array
      
        


