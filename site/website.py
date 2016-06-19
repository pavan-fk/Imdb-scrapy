from flask import Flask, render_template, request, json as flask_json
from DataResource import createDataArray

app = Flask(__name__)


@app.route("/", methods=['GET'])
def mainPage():
    return render_template('home_page.html')


@app.route("/trend", methods=['POST'])
def trendPage():
    searchTerm = request.form['search']
    print(searchTerm)
    return render_template('chart.html', searchTerm=searchTerm)


@app.route('/api', methods=['GET'])
def api():
    response = flask_json.jsonify(createDataArray())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
