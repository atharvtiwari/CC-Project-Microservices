import math

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.secret_key = '080_087_092_111'

class Sine(Resource):
    def __init__(self):
        pass
    
    def get(self, n1, n2):
        try:
            return {"error": False, "result": math.sin(n1 * (math.pi / 180))}
        except Exception as e:
            return {"error": True, "message": str(e)}

api.add_resource(Sine, "/sin/<float(signed=True):n1>/<float(signed=True):n2>")

if __name__ == "__main__":
    app.run(
        debug = True,
        port = 5062,
        host = "0.0.0.0"
    )
