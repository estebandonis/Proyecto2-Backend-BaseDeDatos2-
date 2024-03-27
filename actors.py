from flask import Blueprint, request, jsonify
from flask_restful import Resource, reqparse
from neo4j import GraphDatabase, RoutingControl
from flask import request, jsonify
from Neo4jConnection import Neo4jConnection

import json

api = Blueprint('api/actors', __name__)

conn = Neo4jConnection()

def get_db():
    results = conn.query("MATCH (p:Person) RETURN p.name LIMIT 5")
    return json.dumps(results)

@api.route('/', methods=['GET'])
def home():
    return "Aqui se encuentran los actores"

@api.route('/info', methods=['GET'])
def info():
    names = get_db()
    return names

@api.route('/send', methods=['POST'])
def send_data():
    data = request.get_json()

    print(data)
    # Your API logic here
    return "Actors data received!"
