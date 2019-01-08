from flask import Flask, jsonify, request
from api.models import Redflag, my_red_flags


app = Flask(__name__)

@app.route("/")
def hello_world():
	return "Hello Kato"


#API end point to create a red-flag record
@app.route("/api/v1/red-flags", methods=["POST"])
def create_redflag():
    if not request.json:
        return jsonify({
            "Error": "There is no data returned from the request",
            "status": 400
            }), 400
    data = request.get_json()
    if 'createdBy' not in data or 'comment' not in data or 'type' not in data or 'location' not in data or 'status' not in data:
        return jsonify({'status': 400, 'Error': 'The information is missing'}), 400
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
    	"data": [{ 
        "id":  red_flag._id, 
        "Message": "Created red-flag record"
        }]}), 200



#API end point to fetch all records
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



@app.route("/api/v1/red-flags", methods = [ "GET" ])
def get_all_red_flags():
	if len(my_red_flags) > 0:
		return jsonify({ "status": 200, "data": [red_flag for red_flag in my_red_flags]})
	return jsonify({ "status": 400, "Error": "There are no records"})
 



















