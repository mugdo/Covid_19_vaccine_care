def func_request(user_blueprint, Api,user):
    api = Api(user_blueprint)
    api.add_resource(user, '/user')