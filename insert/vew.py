from os import error
from application import db, Reg, Loger
from application import User
from read import obbejct


def push_user_data():
    for dat in obbejct:
        nid = dat['nid']
        name = dat['name']
        father = dat['father']
        mother = dat['mother']
        date_of_barth = dat['date_of_barth']
        blood_group = dat['blood_group']
        address = dat['address']
        data = User(nid,name,father,mother,date_of_barth,blood_group,address)
        db.session.add(data)
        db.session.commit()
def push_rigister_data():
        nid = 123
        center = "fake"
        date= "1/1/2"
        data = Reg(nid,center,date)
        db.session.add(data)
        db.session.commit()


def push_loger_data():
        for dat in obbejct:
                name = dat['name']
                nid = dat['nid']
                data = Loger(nid,name)
                db.session.add(data)
                db.session.commit()
    
    

