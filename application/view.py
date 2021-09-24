from flask import  request, jsonify
from marshmallow import ValidationError
from flask_restful import Resource
from datetime import  datetime, timedelta
from .router import db,Reg,RegSchema,GetSchema



def get_avalable_date(date):
    res = datetime.strptime(date, "%Y-%m-%d")
    res = (datetime.strptime(res.strftime('%Y-%m-%d'), '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    flag = True
    while flag:
        user_count = Reg.query.filter_by(date = res).count()
        print("user_count :", user_count)
        if user_count>2:
            print("enter")
            res = datetime.strptime(res, "%Y-%m-%d")
            res = (datetime.strptime(res.strftime('%Y-%m-%d'), '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
            print("rest :", res)
            
        else: 
            flag = False
            break 

    return res

def return_response():
    message  = {
        'status': 200,
        'data ': "Registed"
    }
    resp = jsonify(message)
    resp.status_code= 200
    return resp


class Register(Resource):
    def post(self):
        json_requsest = request.get_json()
        try:
            schema = RegSchema()
            result = schema.load(json_requsest)
            date = get_avalable_date(json_requsest['date'])
            data = Reg(result.nid,result.center,date)
            db.create_all()
            db.session.add(data)
            db.session.commit()
            return return_response()
        except ValidationError as err:
            message  = {
                'status': 500,
                'message ': err.messages
                }
            resp = jsonify(message)
            resp.status_code= 500
            return resp
            

    def get(self):

        _json = request.json
        date = _json['date']
        user_array =[]
        user_data = Reg.query.filter_by(date = date)
        # for user in user_data:
        post_schema = GetSchema(many=True)
        Schema = post_schema.dump(user_data) 
        user_array.append(Schema)
    
        message  = {
            'date': date,
            'status': 200,
            'data ': Schema
        }
        resp = jsonify(message)
        resp.status_code= 200
        return resp
    

        



    

        
    



 
