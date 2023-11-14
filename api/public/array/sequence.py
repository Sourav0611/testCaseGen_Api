from flask import jsonify
from flask_restful import Resource, reqparse
import random

class SequentialArray(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('s', required=True, type=int, help='Start is missing.', location='args')
        parser.add_argument('e', required=True, type=int, help='End is missing.', location='args')
        parser.add_argument('i', required=True, type=int, help='Increment is missing.', location='args')
        parser.add_argument('r', type=int, location='args')
        args = parser.parse_args()

        s, e, i, r = args['s'], args['e'], args['i'], args['r']

        if i == 0 or s < e and i <= 0 or s > e and i >= 0:
            return jsonify({'data': None})

        sequence = [x for x in range(s, e, i)]
        if r == 1:
            random.shuffle(sequence)
        return jsonify({'data': sequence})
