from flask import Blueprint
from flask import  render_template, url_for
import mysql


# Blueprint Configuration
home_bp = Blueprint('home_bp', __name__,template_folder='home/templates')

__all__ = ['index','record_view']

#Routes
@home_bp.route('/', methods=['GET'])
def index():
    user = {'username': 'BioStats'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostatsImport')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, biostats=result)

@home_bp.route('/view/<int:biostats_id>', methods=['GET'])
def record_view(biostats_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostatsImport WHERE id=%s', biostats_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', biostats=result[0])