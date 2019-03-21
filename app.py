# Note: We are importing “Flask” , “Api” and “Resource” with capital letter initials,
# it signifies that a class is being imported.
# reqparse is Flask-RESTful request parsing interface which will be used later on.
# Then we create an app using “Flask” class, “__name__” is a Python special variable
# which gives Python file a unique name, in this case, we are telling the app to run
# in this specific place

from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Nick",
        "age": 20,
        "occupation": "Postman"
    },
    {
        "name": "Paul",
        "age": 25,
        "occupation": "Doctor"
    },
    {
        "name": "Rob",
        "age": 20,
        "occupation": "Engineer"
    }
]


class User(Resource):

    def get(self, name):
        # The get method is used to retrieve a particular user details by specifying the name:
        # We will traverse through our users list to search for the user,
        # if the name specified matched with one of the user in users list,
        # we will return the user, along with '200 OK',
        # else return a user not found message with '404 Not Found'.
        # Another characteristic of a well designed REST API is that it uses
        # standard HTTP response status code to indicate whether a request
        # is being processed successfully or not.
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name, occupation):
        # The post method is used to create a new user:
        # We will create a parser by using reqparse we imported earlier,
        # add the age and occupation arguments to the parser,
        # then store the parsed arguments in a variable,
        # args (the arguments will come from request body in the form of form-data, JSON or XML).
        # If a user with same name already exists,
        # the API will return a message along with '400 Bad Request',
        # else we will create the user by appending it to users list and
        # return the user along with '201 Created'.
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": occupation
        }
        users.append(user)
        return user, 201

    def put(self, name):
        # The put method is used to 'update' details of user,
        # or create a new one if it is not existed yet.
        # If the user already exist, we will update their details with the parsed arguments
        # and return the user along with '200 OK',
        # else we will create and return the user along with '201 Created'.
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        # The delete method is used to delete user that is no longer relevant:
        # By specifying users as a variable in global scope,
        # we update the users list using list comprehension to create a list without the name
        # specified (simulating delete), then return a message along with '200 OK'.
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200


# Finally, we have done implementing all the methods in our User resource,
# we will add the resource to our API and specify its route,
# then run our Flask application:
api.add_resource(User, "/user/<string:name>")
api.add_resource(
    User, "/user/<string:name>/occupation/<string:occupation>", endpoint="occ")

app.run(debug=True)
