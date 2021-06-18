"""from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
"""

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

import mutante
app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def get():
    return {"mensaje":"** liga de magneto **"},200

@app.route('/mutant', methods=['POST'])
def post():
    dna=null
    parser = reqparse.RequestParser()
    parser.add_argument("dna")
    params = parser.parse_args()
    dna=params["dna"]
    return params
"""
    print(dna,type(dna))
    if mutante.isAdn(dna):
        if mutante.isMutant(dna):
            return 200
        else:
            return 403
"""
if __name__ == "__main__":
    app.run()
