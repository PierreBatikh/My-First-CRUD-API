from flask import Flask, jsonify, request
from datetime import date
import json

BDs = 0

try:
    with open("friends.json", "r") as file:
        BDs = json.load(file)
        if not isinstance(BDs, list):
            BDs = []
except (FileNotFoundError, json.JSONDecodeError):
    BDs = []


app = Flask(__name__)



@app.route("/")
def index():
    return "Welcome to the freinds BDs API"

@app.route("/all", methods=["GET"])
def all():
    return jsonify([bd for bd in BDs]), 200

@app.route("/today", methods=["GET"])
def today():
    bdays = []
    today_date = date.today().strftime("%#d-%B")
    for bd in BDs:
        if bd["birthday"] == today_date:
            bdays.append({"message": "Happy Birthday!", "person": bd})
    if bdays:    
        return jsonify(bdays), 200 
    else:
        return jsonify({"message": "No birthday today"}), 200

@app.route("/month", methods=["GET"])
def month():
    bdays = []
    today_date = date.today().strftime("%#d-%B")
    for bd in BDs:
        if bd["birthday"].split("-")[1] == today_date.split("-")[1]:
            bdays.append(bd)
    if bdays:    
        return jsonify(bdays), 200 
    else:
        return jsonify({"message": "No birthday today"}), 200

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    name = data.get("Name")
    bd = data.get("birthday")
    to_append = {"Name": name, "birthday": bd}
    BDs.append(to_append)
    with open("friends.json", "w") as file:
        json.dump(BDs, file, indent=4)
    return jsonify(to_append), 201

@app.route("/update/<string:name>", methods=["PUT"])
def update(name):
    data = request.get_json()
    new_name = data.get("Name")
    new_bd = data.get("birthday")
    for bd in BDs:
        if bd["Name"] == name:
            bd["Name"] = new_name
            bd["birthday"] = new_bd
            break
    else:
        return "", 404
    with open("friends.json", "w") as file:
        json.dump(BDs, file, indent=4)
    return "", 200


@app.route("/remove/<string:name>", methods=["DELETE"])
def remove(name):
    for bd in BDs:
        if bd["Name"] == name:
            BDs.remove(bd)
            break
    else:
        return "", 404
    with open("friends.json", "w") as file:
        json.dump(BDs, file, indent=4)
    return "", 204



if __name__ == "__main__":
    app.run(debug=True)
