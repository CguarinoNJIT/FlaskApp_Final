from flask import Blueprint
from flask import  request, redirect, render_template
from __init__ import db_var


# Blueprint Configuration
form_bp = Blueprint('form_bp', __name__,template_folder='form/templates')

__all__ = ['form_edit_get','form_update_post','form_insert_get','form_insert_post','form_delete_post']

@form_bp.route('/edit/<int:biostats_id>', methods=['GET'])
def form_edit_get(biostats_id):
    cursor = db_var.get_db().cursor()
    cursor.execute('SELECT * FROM biostatsImport WHERE id=%s', biostats_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', biostats=result[0])

@form_bp.route('/edit/<int:biostats_id>', methods=['POST'])
def form_update_post(biostats_id):
    cursor = db_var.get_db().cursor()
    inputData = (request.form.get('Name'), request.form.get('Sex'), request.form.get('Age'),
                 request.form.get('Height_in'), request.form.get('Weight_lbs'), biostats_id)
    sql_update_query = """UPDATE biostatsImport t SET t.Name = %s, t.Sex = %s, t.Age = %s, t.Height_in = 
    %s, t.Weight_lbs = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    db_var.get_db().commit()
    return redirect("/", code=302)

@form_bp.route('/biostats/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Profile')

@form_bp.route('/biostats/new', methods=['POST'])
def form_insert_post():
    cursor = db_var.get_db().cursor()
    inputData = (request.form.get('Name'), request.form.get('Sex'), request.form.get('Age'), request.form.get('Height_in'), request.form.get('Weight_lbs'))
    sql_insert_query = """INSERT INTO biostatsImport (Name,Sex,Age,Height_in,Weight_lbs) VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(sql_insert_query, inputData)
    db_var.get_db().commit()
    return redirect("/", code=302)

@form_bp.route('/delete/<int:biostats_id>', methods=['POST'])
def form_delete_post(biostats_id):
    cursor = db_var.get_db().cursor()
    sql_delete_query = """DELETE FROM biostatsImport WHERE id = %s """
    cursor.execute(sql_delete_query, biostats_id)
    db_var.get_db().commit()
    return redirect("/", code=302)