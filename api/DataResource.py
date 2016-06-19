from flask import Flask, json
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/api', methods=['GET'])
def login():
    response = json.jsonify({"x": 10, "y": 21, "label": "episode1"}, {"x": 20, "y": 25}, {
                            "x": 30, "y": 20}, {"x": 40, "y": 25}, {"x": 50, "y": 27})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# todo: remove debug mode
if __name__ == '__main__':
    app.run(debug=True)
