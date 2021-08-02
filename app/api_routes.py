from flask import Blueprint
import simplejson as json
from flask import  request, Response
from __init__ import db_var

# Blueprint Configuration
api_bp = Blueprint('api_bp', __name__)

__all__ = ['api_browse', 'api_retrieve','api_add','api_edit','api_delete']

@api_bp.route('/api/v1/biostats', methods=['GET'])
def api_browse() -> Response:
    cursor = db_var.get_db().cursor()
    cursor.execute('SELECT * FROM biostatsImport')
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp

@api_bp.route('/api/v1/biostats/<int:biostats_id>', methods=['GET'])
def api_retrieve(biostats_id) -> Response:
    cursor = db_var.get_db().cursor()
    cursor.execute('SELECT * FROM biostatsImport WHERE id=%s', biostats_id)
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp

#This will add a record to the JSON Database
@api_bp.route('/api/v1/biostats', methods=['POST'])
def api_add() -> Response:
    content = request.json
    cursor = db_var.get_db().cursor()
    inputData = (content['Name'], content['Sex'], content['Age'], content['Height_in'], request.form.get('Weight_lbs'))
    sql_insert_query = """INSERT INTO biostatsImport (Name,Sex,Age,Height_in,Weight_lbs) VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(sql_insert_query, inputData)
    db_var.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp

#This will allow edits to a record and update the JSON Database.
@api_bp.route('/api/v1/biostats/<int:biostats_id>', methods=['PUT'])
def api_edit(biostats_id) -> Response:
    cursor = db_var.get_db().cursor()
    content = request.json
    inputData = (content['Name'], content['Sex'], content['Age'], content['Height_in'], content['Weight_lbs'], biostats_id)
    sql_update_query = """UPDATE biostatsImport t SET t.Name = %s, t.Sex = %s, t.Age = %s, t.Height_in = %s, t.Weight_lbs = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    db_var.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp

#This will delete a record and update the JSON Database.
@api_bp.route('/api/v1/biostats/<int:biostats_id>', methods=['DELETE'])
def api_delete(biostats_id) -> Response:
    cursor = db_var.get_db().cursor()
    sql_delete_query = """DELETE FROM biostatsImport WHERE id = %s """
    cursor.execute(sql_delete_query, biostats_id)
    db_var.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp
