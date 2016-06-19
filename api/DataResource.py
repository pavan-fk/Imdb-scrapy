from flask import Flask, json as flask_json
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


@app.route('/api', methods=['GET'])
def api():
    a = []
    episodeNumber = 1
    for episode in json.load(open("/Users/pavan.k/Code/tv-trends/data/star_trek.json")):
        a.append({"x": episodeNumber,
                  "y": float(episode["episodeRating"]), "toolTipContent": episode["title"]})
        episodeNumber = episodeNumber + 1
    response = flask_json.jsonify(a)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# todo: remove debug mode
if __name__ == '__main__':
    app.run(debug=True)
