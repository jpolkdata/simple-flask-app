"""
data_model.py
---------------
Implements the data layer for this app by simulating a database. 

Rather than configure a DB connection we just use a JSON file 
with a simple dataset.
"""

import json

def load_db():
    with open("superheroes.json") as f:
        return json.load(f)

def save_db():
    with open("superheroes.json", 'w') as f:
        return json.dump(db, f)

db = load_db()