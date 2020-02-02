
import os
from flask import Flask, request, jsonify
from app.data_utilities import load_data_file

app = Flask(__name__)


@app.route('/')
def index():
    return "Home"


@app.route('/api/ks', methods=['GET'])
def get_cities():
    # Get data file
    project_folder = _project_directory()
    data = load_data_file(f"{project_folder}/data/ks_cities.txt")
    results = {
        'data': data
    } 
    return jsonify(results)

def _project_directory():
    current_file = __file__  # ../project/app/app.py
    app_folder = os.path.dirname(current_file)  # ../project/app
    project_folder = os.path.dirname(app_folder)  # ../project
    return project_folder