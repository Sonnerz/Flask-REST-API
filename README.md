# Flask-REST-API

$ python -m flask run

api.add_resource(User, "/user/<string:name>")
api.add_resource(User, "/user/<string:name>/occupation/<string:occupation>", endpoint="occ")


##	Postman
open GET 127.0.0.1/user/Rob
open POST 127.0.0.1/user/Rob/occupation/farmer


###	 it took a while for postman to find 127.0.0.1, try restarting.
