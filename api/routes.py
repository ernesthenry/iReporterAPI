from flask import Flask, jsonify, request
from models import Redflag, my_red_flags


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello Kato"


@app.route("/api/v1/red-flags", methods=["POST"])
def create_redflag():
    data = request.get_json()
    red_flag = Redflag(
    		data["createdBy"], data["type"],
        	data["location"], data["status"], data["Images"],
        	data["Videos"], data["comment"]
       	   )
    my_red_flags.append(
    	red_flag.format_record()
    	)
    if len(my_red_flags) == 0:
    	return jsonify({
    		"status": 400, 
    		"Error": "Invalid request"
    		})
    return jsonify({
    	"status": 201,
    	"data": red_flag.format_record()
    	})


@app.route("/api/v1/red-flags", methods=["GET"])
def get_all_red_flags():
    if len(my_red_flags) > 0:
        return jsonify({
        	"status": 200,
            "data": [red_flag for red_flag in my_red_flags]
        	})
    return jsonify({
    	"status": 400,
    	"Error": "There are no records"
   		})


@app.route("/api/v1/red-flags/<int:flag>", methods=["GET"])
def get_a_redflag(flag):
    redflag = [red_flag for red_flag in my_red_flags if red_flag['id'] == flag]
    if redflag:
        return jsonify({
        	"redflag": redflag
        	})
    return jsonify({
    	"status": 404,
        "Error": " Invalid record"
    	})


@app.route("/api/v1/red-flags/<int:id>", methods=["DELETE"])
def delete_red_flag(id):
    #redflag = [red_flag for red_flag in my_red_flags if red_flag['id'] == id]
    for red_flag in my_red_flags:
    	if red_flag["id"] == id:
    		return red_flag
    if len(my_red_flags) == 0:
        return jsonify({
        	"status": "400",
            "Error": "Invalid request"
        	})
    my_red_flags.remove(red_flag[0])
    return jsonify({
    	'result': True
    	})



