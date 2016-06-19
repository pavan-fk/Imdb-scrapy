from flask import Flask, json as flask_json
from flask_restful import Resource, Api
import json
import random

app = Flask(__name__)
api = Api(app)


def createDataArray():
    dataArray = []
    dataArrayObject = {}
    dataArrayObject["type"] = "line"
    dataPoints = []
    for episode in json.load(open("/Users/pavan.k/Code/tv-trends/data/star_trek.json")):
        dataPoints.append(createDataPoint(episode))
    dataArrayObject["dataPoints"] = dataPoints
    dataArray.append(dataArrayObject)
    return dataPoints


def createDataPoint(episodeObject):
		season = int(episodeObject["season"])
		return {"x": int(episodeObject["episode"])+int(episodeObject["season"]), "y": float(episodeObject["episodeRating"]), "toolTipContent": episodeObject["title"], "markerColor":"#ffaaee"}


@app.route('/api', methods=['GET'])
def api():
    response=flask_json.jsonify(createDataArray())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# todo: remove debug mode
if __name__ == '__main__':
    app.run(debug=True)
