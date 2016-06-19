from flask import Flask, json as flask_json
from flask_restful import Resource, Api
import json
import random

app = Flask(__name__)
api = Api(app)


colors=["#00aedb","#a200ff","#f47835","#d41243","#8ec127"]

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
		return {"x": int(episodeObject["episode"])+int(episodeObject["season"]), "y": float(episodeObject["episodeRating"]), "toolTipContent": episodeObject["title"], "markerColor":colors[int(episodeObject["season"])]}


@app.route('/api', methods=['GET'])
def api():
    response=flask_json.jsonify(createDataArray())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# todo: remove debug mode
if __name__ == '__main__':
    app.run(debug=True)
