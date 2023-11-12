from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
CORS(app)
api = Api(app)

class Home(Resource):
    def get(self):
        return jsonify({'name': 'texpregen API Server'})

# Routes
api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run()
