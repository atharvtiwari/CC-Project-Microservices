import math

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.secret_key = '080_087_092_111'

class LCM(Resource):
    def __init__(self):
        pass
    
    def get(self, n1, n2):
        try:
            gcd = float(math.gcd(int(n1), int(n2)))
            return (0 if gcd == 0 else (abs(n1 * n2) / gcd))
        except Exception as e:
            return str(e)

api.add_resource(LCM, "/lcm/<float(signed=True):n1>/<float(signed=True):n2>")

if __name__ == "__main__":
    app.run(
        debug = True,
        port = 5056,
        host = "0.0.0.0"
    )
