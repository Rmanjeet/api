from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/<string:name>', methods=['GET'])
def index(name):
    return jsonify({"API":"This ia a GET API",
                    "Request " : name})

@app.route('/', methods=['POST'])
def post():
    data = request.get_json(force=True) 
    return jsonify({"API":"This is a POST request",
                    "Request": data})