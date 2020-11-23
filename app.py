#imort library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#inisiasi object flask 
app = Flask(__name__)

#inisiasi object flask_restful
api = Api(app)

#inisiasi object cors
CORS(app)

#membuatResource
class AwalResource(Resource):
    #metode dalam rest api
    def get(self):
        response = {"msg" : "Hallo Eko HIdayat, Ini contoh restful python"}
        return response
   
#setup resource
api.add_resource(AwalResource, "/api", methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True, port=8080)