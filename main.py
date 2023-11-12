from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource

from api.public.array.sequence import SequentialArray

app = Flask(__name__)
CORS(app)
api = Api(app)

class Home(Resource):
    def get(self):
        return jsonify({'name': 'texpregen API Server'})

# Routes
api.add_resource(Home, '/')
api.add_resource(SequentialArray, '/array')

if __name__ == '__main__':
    app.run()
