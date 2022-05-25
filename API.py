from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/<string:name>", methods=["GET"])
def get(name):
    return jsonify({"hello": name})

@app.route("/", methods=["POST"])
def post():
    data = request.json
    return jsonify({"your data": data})