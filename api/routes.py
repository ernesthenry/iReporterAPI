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
        "id": red_flag._id,
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
        "Error": " Invalid record"
    	})


# API end point to delete a specific record
@app.route("/api/v1/red-flags/<int:flag_id>", methods=["DELETE"])
def delete_red_flag(flag_id):
    red_flag_record = [flag for flag in my_red_flags if flag['id'] == flag_id]
    if len(my_red_flags) == 0:
        return jsonify({
        	"status": "400",
            "Error": "Invalid request"
        	})
    my_red_flags.remove(red_flag_record[0])
    return jsonify({
    	'result': True
    	}), 200


# API end point to edit location of  red-flag record
@app.route("/api/v1/red-flags/<int:flag_id>/location", methods=["PATCH"])
def edit_red_flag_location(flag_id):
    data = request.get_json()
    red_flag_record = [
    red_flag for red_flag in my_red_flags if red_flag['id'] == flag_id
    ]
    
    if not red_flag_record:
        return jsonify({
                        "status": "400",
                        "Error": "Red flag is not available"
                        })
    red_flag_record[0].location = data["location"]
    return jsonify({
                     "status" : 200, "data": [{
                     "id": "flag_id", 
                     "message": "Updated red-flag's record location"
                     }]
                  }), 200

# API end point to edit comment of a  red-flag record
@app.route("/api/v1/red-flags/<int:flag_id>/comment", methods=["PATCH"])
def edit_red_flag_comment(flag_id):
    data = request.get_json()
    red_flag_record = [
    red_flag for red_flag in my_red_flags if red_flag['id'] == flag_id
    ]
    if not red_flag_record:
        return jsonify({
                        "status": "400",
                        "Error": "Red flag is not available"
                        })
    red_flag_record[0].comment = data["comment"]
    return jsonify({
                     "status" : 200, "data": [{
                     "id": "flag_id",
                     "message": "Updated red-flag's record comment"
                     }]

                    }), 200


 



















