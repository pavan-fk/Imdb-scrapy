from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api=Api(app)


class DataResource(Resource):
    def get():
        return "Hello world"


api.add_resource(DataResource,"/")

# todo: remove debug mode
if __name__ == '__main__':
    app.run(debug=True)
