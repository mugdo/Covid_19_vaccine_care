from flask import Flask 
from application import user_blueprint
from core import db
from insert import push_user_data, push_rigister_data, push_loger_data
from flask_login import LoginManager



APP = Flask('__name__')
APP.run(debug=True)


APP.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@172.18.0.2/test'
APP.config['SECRECT_KEY'] = 'secrectkey'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


APP.register_blueprint(user_blueprint)
login_manager = LoginManager()
login_manager.init_app(APP)
with APP.app_context():

    db.init_app(APP)
    db.create_all()
    # push_user_data()
    # push_rigister_data()
    # push_loger_data()
    db.session.commit()

if __name__ == "__main__":
    APP.secret_key = 'super secret key'
    APP.run() 