from flask import Flask
from  service.vew import user_blueprint


app = Flask('__name__')
app.debug=True

app.register_blueprint(user_blueprint)
