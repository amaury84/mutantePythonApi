"""from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
"""
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
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
import json

import mutante
app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def get():
    return {"mensaje":"** liga de magneto **"},200

@app.route('/mutant', methods=['POST'])
def post():
    dna=request.data
    dna = str(dna)
    #limpiamos el string antes de hacerlo lista
    dna = dna.replace("b","")
    #dna = dna.replace("[","")
    #dna = dna.replace("]","")
    dna = dna.replace("\'","")
    #hacemos el string una lista
    #dna = dna.split(",")
    dna = json.loads(dna)
    #tipo = type(dna["dna"])
    dnalist=dna["dna"]
    #return str(dnalist)
    
    if mutante.isAdn(dnalist):
        if mutante.isMutant(dnalist):
            return "HTTP-OK",200
        else:
            return "HTTP-FORBIDEN",403

if __name__ == "__main__":
    app.run()
