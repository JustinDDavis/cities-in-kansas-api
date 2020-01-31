
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/ks', methods=['GET'])
def get_cities():
    data = "Data to be implemented"
    # Prepare data that may have been filtered
    results = {
        'data' : data
    } 
    return jsonify(results)

