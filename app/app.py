
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Home"

@app.route('/api/ks', methods=['GET'])
def get_cities():
    data = "Data to be implemented"
    results = {
        'data' : data
    } 
    return jsonify(results)

