import marshmallow
from marshmallow.exceptions import ValidationError
from .router import db
from marshmallow import Schema, fields, post_load, validates,validate
from datetime import  datetime, timedelta
from flask_login import UserMixin, LoginManager

class Reg(db.Model):
    __tablename__ = 'register'
    id =db.Column(db.Integer, primary_key = True)
    nid = db.Column(db.Integer)
    center = db.Column(db.String(100))
    date = db.Column(db.Date())
    def __init__(self,nid, center, date):
        self.nid = nid
        self.center = center
        self.date = date 
    # def __repr__(self):
    #     return f'{self.nid} is registed {self.center} center date : {self.date}' 
class User(db.Model):
    __tablename__ = 'user'
    id =db.Column(db.Integer, primary_key = True)
    nid = db.Column(db.Integer)
    name = db.Column(db.String(20))
    father = db.Column(db.String(20))
    mother = db.Column(db.String(20))
    date_of_barth = db.Column(db.Date())
    blood_group = db.Column(db.String(10))
    address = db.Column(db.String(100))
    def __init__(self,nid, name, father, mother, date_of_barth, blood_group, address):
        self.nid = nid
        self.name = name
        self.father = father
        self.mother = mother 
        self.date_of_barth = date_of_barth
        self.blood_group = blood_group
        self.address = address


def valided_date(date):
    if date.day < datetime.now().day:
        raise ValidationError('Your have to give valid day')
    elif date.month < datetime.now().month:
        raise ValidationError('Your have to give valid month')
    elif date.year < datetime.now().year:
        raise ValidationError('Your have to give valid year')
def valided_nid(nid):
    if User.query.filter_by(nid = nid).first():
        if Reg.query.filter_by(nid = nid).first():
            raise ValidationError('Allready Registed')
        else:
            return True
    else:
        raise ValidationError('nid is not valid')  

class RegSchema(Schema):
    nid = fields.Integer(validate = valided_nid)
    center = fields.String()
    date = fields.Date(validate = valided_date)
    @post_load
    def do_register(self, data, **kwargs):
        return Reg(**data)
    

class GetSchema(Schema):
    nid = fields.Integer()
    center = fields.String()

# class PostSchema(ma.Schema):
#     class Meta:
#         fields = ("nid", "center", "date")

login_manager = LoginManager()
class Loger(UserMixin,db.Model):
    id =db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))

    def __init__(self,id, username):
        self.nid = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    return Loger.query.get(int(user_id)).first()





class LogerSchema(Schema):
    nid = fields.Integer()
    username = fields.String()
















