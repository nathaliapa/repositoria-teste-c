from flask import Flask
from flask_restful import Api, Resource
from connection import getTopicos

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        #return{"data": "Hello World"}
        return getTopicos()

api.add_resource(HelloWorld, "/hello")

if __name__ == "__main__":
    app.run(debug=True)