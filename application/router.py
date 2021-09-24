from core import db,ma
from .model import Reg,RegSchema,User,GetSchema
from flask import Blueprint
from flask_restful import  Api
user_blueprint = Blueprint('user',__name__,url_prefix="/user")
from .view import Register
api = Api(user_blueprint)
api.add_resource(Register, '/user')
