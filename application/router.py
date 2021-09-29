from core import db,ma
from .model import Reg,RegSchema,User,GetSchema, Loger
from flask import Blueprint
from flask_restful import  Api
user_blueprint = Blueprint('user',__name__,url_prefix="/application")
from .view import Register,Login

api = Api(user_blueprint)

api.add_resource(Register, '/user')
api.add_resource(Login,'/login')
