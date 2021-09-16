from flask import Flask


app = Flask('__name__')
app.debug=True


from service.vaccin_care import blueprint
app.register_blueprint(blueprint)
