from flask import jsonify, request
from src.Model.Model_tech import  get_all_technologies, add_technology, update_technology, delete_technology, get_technology_by_id


def fetch_all_technologies():
    technologies = get_all_technologies()
    
    result = []
    for technology in technologies:
        result.append({
            "id": technology["id"],
            "name": technology["name"]
        })
    
    return jsonify(result), 200


#==================================================================================================

def fetch_technology_by_id(technology_id):
    technology = get_technology_by_id(technology_id)
    
    if not technology:
        return jsonify({"error": "Technology not found"}), 404
    
    return jsonify({
        "id": technology["id"],
        "name": technology["name"]
    }), 200
    
#==================================================================================================

def attach_technology():
    data = request.get_json()
    
    name = data.get("name")
    
    if not name:
        return jsonify({"error": "name is required"}), 400
    
    technology_id = add_technology(name)
    
    return jsonify({"id": technology_id, "name": name}), 201

#==================================================================================================

def edit_technology(technology_id):
    data = request.get_json()
    
    name = data.get("name")
    
    if not name:
        return jsonify({"error": "name is required"}), 400
    
    update_technology(technology_id, name)
    
    return jsonify({"id": technology_id, "name": name}), 200

#==================================================================================================

def remove_technology(technology_id):
    
    delete_technology(technology_id)
    
    return jsonify({"id": technology_id}), 200