
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import sys
import os

app = Flask(__name__)
CORS(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Building

@app.route('/getall', methods=['GET'])
def get_all():
    try:
        buildings=Building.query.all()
        return  jsonify([e.serialize() for e in buildings])
    except Exception as e:
	    return(str(e))

@app.route('/api/simplelist', methods=['GET'])
def hello():
    return jsonify({'Item 1':'chicken', 'Item 2':'steak', 'Item 3':'wegetarian for Raghav'})

print(sys.path)
