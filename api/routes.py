from flask import Flask, jsonify, request
from models import Redflag, my_red_flags


app = Flask(__name__)


@app.route("/")
def hello_world():
	return "Hello Kato"


@app.route("/api/v1/red-flags", methods=["POST"])
def create_redflag():
	data = request.get_json()
	red_flag = Redflag(data["createdBy"], data["type"], data["location"], data["status"], data["Images"],
	 data["Videos"], data["comment"])

	my_red_flags.append(red_flag.format_record())
	return jsonify({"status": 201, "data": red_flag.format_record()})

@app.route("/api/v1/red-flags", methods = [ "GET" ])
def get_all_red_flags():
	if len(my_red_flags) > 0:
		return jsonify({ "status": 200, "data": [red_flag for red_flag in my_red_flags]})
	return jsonify({ "status": 400, "Error": "There are no records"})
	
@app.route("/api/v1/red-flags/<int:id>", methods = [ "GET" ])
def get_a_redflag(id):
	redflag = [red_flag for red_flag in my_red_flags if red_flag['id'] == id]
	my_red_flags.append(red_flag)
	if red_flag:
		return jsonify({'redflag': red_flag})
	return jsonify({ "status": 404, "Error": " Invalid record"})
 



















