
from flask import Flask, request, jsonify

from app.data_utilities import load_data_file

app = Flask(__name__)


@app.route('/')
def index():
    return "Home"


@app.route('/api/ks', methods=['GET'])
def get_cities():
    data = load_data_file('ks_cities.txt')
    results = {
        'data': data
    } 
    return jsonify(results)

