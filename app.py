from flask import Flask 
from application import user_blueprint
from core import db
from insert import push_user_data, push_rigister_data



APP = Flask('__name__')


APP.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://shaiful:''@localhost/Users'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

APP.register_blueprint(user_blueprint)
with APP.app_context():

    db.init_app(APP)
    db.create_all()
    # push_user_data()
    # push_rigister_data()
    db.session.commit()

if __name__ == "__main__":
    APP.run(port =9000) 


     