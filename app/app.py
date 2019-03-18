
from flask import Flask, request, jsonify
from db.db import Database

from app.tools import filter_items

db = Database()
db.connect()

app = Flask(__name__)

@app.route('/api/ks', methods=['GET'])
def get_cities():
    # Prepare URL Arguments
    starts_with = request.args.get('startswith')

    # Collect Values from database
    values_from_database = db.cities()
    
    # Start Filtering what values should be returned
    results = []
    if starts_with:
        data = filter_items(starts_with, values_from_database)
    else:
        data = values_from_database
    
    # Prepare data that may have been filtered
    results = {
        'data' : data
    } 
    return jsonify(results)

