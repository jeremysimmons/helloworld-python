from flask import Flask, request
from flask_restful import Resource, Api

class Greeting (Resource):
   def get(self):
      return { "message" : "Hello Flask API World!", "version": 2 }

app = Flask(__name__)
api = Api(app)
api.add_resource(Greeting, '/')

if __name__ == '__main__':
   app.run('0.0.0.0','8080')

