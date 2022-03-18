from flask import make_response, jsonify

def success(values):
    res = {
        "status" : 200,
        "length" : len(values),
        "data" : values
    }
    return make_response(jsonify(res), 200)