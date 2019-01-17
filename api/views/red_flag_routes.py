from flask import Flask, jsonify, request
from api.models.red_flag_incident import Redflag, my_red_flags
from api import app




@app.route("/")
def home():
    """A welcoming route to my api"""

    return jsonify({
        'message': 'Welcome to ernest\'s iReporter app.',
        'status': '200'
    }), 200

#API end point to create a red-flag record
@app.route("/api/v1/red-flags", methods=["POST"])
def create_redflag():
    data = request.get_json()

    created_by = data.get("createdBy")
    incident_type = data.get("type")
    red_flag_status = data.get("status")
    images = data.get("Images")
    red_flag_location = data.get("location")
    videos = data.get("Videos")
    comments = data.get("comment")

    if not created_by or not incident_type or not red_flag_location \
    or not red_flag_status or not images or not videos or not comments:
        return jsonify({
            "Error": "Required field is missing"
        }), 400
        
    for comment in my_red_flags:
        if comment["comment"] == comments:
            return jsonify({
            "Error": "Redflag record exists",
            "status": 400

        }), 400 

    red_flag = Redflag(
    		created_by,  incident_type, red_flag_location, red_flag_status, images,
        	videos, comments
       	   )
    my_red_flags.append(
    	red_flag.format_record()
    	)
    if len(my_red_flags) == 0:
    	return jsonify({
    		"status": 400, 
    		"Error": "Invalid request"
    		}), 400
    return jsonify({
    	"data": red_flag.format_record(),  
        "status": 201,            
        "Message": "Created red-flag record" 
        }), 201



#API end point to fetch all records
@app.route("/api/v1/red-flags", methods=["GET"])
def get_all_red_flags():
    if len(my_red_flags) > 0:
        return jsonify({
        	"status": 200,
            "data": [red_flag for red_flag in my_red_flags]
        	}), 200
    return jsonify({
    	"status": 400,
    	"Error": "There are no records"
   		})

#API end point to fetch a specific record
@app.route("/api/v1/red-flags/<int:flag_id>", methods=["GET"])
def get_a_redflag(flag_id):
    red_flag_record= [red_flag for red_flag in my_red_flags if red_flag['id'] == flag_id]
    if red_flag_record:
        return jsonify({
            "status": 200,
        	"redflag": red_flag_record
        	}), 200
    return jsonify({
    	"status": 404,
        "Error": " Record does not exist"
    	}), 404

# API end point to delete a specific record
@app.route("/api/v1/red-flags/<int:flag_id>", methods=["DELETE"])
def delete_red_flag(flag_id):
    red_flag_record = [flag for flag in my_red_flags if flag['id'] == flag_id]
    if len(my_red_flags) == 0:
        return jsonify({
        	"status": "200",
            "Error": "There is nothing found"
        	}), 200
    my_red_flags.remove(red_flag_record[0])
    return jsonify({
    	'Result': "record was deleted successfully"
    	}), 200




 # API end point to edit location of  red-flag record
@app.route("/api/v1/red-flags/<int:flag_id>/location", methods=["PATCH"])
def edit_red_flag_location(flag_id):
    data = request.get_json()

    for red_flag_record in my_red_flags:
        if red_flag_record['id'] == flag_id:
            red_flag_record["location"] = data["location"]
            return jsonify({
                "data": red_flag_record,
                "status" : 200,
                "message": "Updated red-flag's record location"
            }), 200
    
    
    if not red_flag_record:
        return jsonify({
                         "status": "400",
                        "Error": "Red flag is not available"
                        }), 400

# API end point to edit comment of a  red-flag record
@app.route("/api/v1/red-flags/<int:flag_id>/comment", methods=["PATCH"])
def edit_red_flag_comment(flag_id):
    data = request.get_json()
    for red_flag_record in my_red_flags:
        if red_flag_record['id'] == flag_id:
            red_flag_record["comment"]= data["comment"]
            return jsonify({
               "data": red_flag_record,
               "status" : 200, 
                "message": "Updated red-flag's record comment"
                }), 200
    if not red_flag_record:
        return jsonify({
                        "status": "400",
                        "Error": "Red flag is not available"
                        })
   
            

 



















