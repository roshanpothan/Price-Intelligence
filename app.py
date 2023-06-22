from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
from scrappers import get_items

app = Flask(__name__)
api = Api(app)


class home(Resource):
    def get(self):
        return jsonify(
            {
                'messgage': 'success',
                'status': 200
            }
        )
class wegmans(Resource):
    def get(self):
        args = request.args
        keyword = args['keyword']
        return jsonify(get_items(keyword))


api.add_resource(home, '/')
api.add_resource(wegmans, '/wegmans')

if __name__ == "__main__":
    app.run(debug=True)