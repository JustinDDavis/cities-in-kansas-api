
from flask import Flask, request, jsonify, render_template
from app.data_utilities import load_data_file, _project_directory, merged_city_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/ks', methods=['GET'])
def get_cities():
    # Get data file
    project_folder = _project_directory()
    data = load_data_file(f"{project_folder}/data/ks_cities.txt")
    results = {
        'data': data
    } 
    return jsonify(results)

@app.route('/api/ks/cities')
def get_filtered_cities():
    city_payload = merged_city_data()

    final_payload = {
        "data": city_payload
    }
    return jsonify(final_payload)
