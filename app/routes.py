import simplejson as json
from flask import request, Response, redirect, render_template, url_for, make_response
from datetime import datetime as dt
from models import User
from forms import ContactForm, SignupForm
from __init__ import mysql, app, db

__all__ = ['index','record_view','form_edit_get','form_update_post',
           'form_insert_get','form_insert_post','form_delete_post','api_browse',
           'api_retrieve','api_add','api_edit','api_delete','contact','user_records','create_user','success']

#Homepage
@app.route('/', methods=['GET'])
def index():
    user = {'username': 'BioStats'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostatsImport')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, biostats=result)

#View Record
@app.route('/view/<int:biostats_id>', methods=['GET'])
def record_view(biostats_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostatsImport WHERE id=%s', biostats_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', biostats=result[0])

# Edit page
@app.route('/edit/<int:biostats_id>', methods=['GET'])
def form_edit_get(biostats_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostatsImport WHERE id=%s', biostats_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', biostats=result[0])

#Update DB
@app.route('/edit/<int:biostats_id>', methods=['POST'])
def form_update_post(biostats_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Name'), request.form.get('Sex'), request.form.get('Age'),
                 request.form.get('Height_in'), request.form.get('Weight_lbs'), biostats_id)
    sql_update_query = """UPDATE biostatsImport t SET t.Name = %s, t.Sex = %s, t.Age = %s, t.Height_in = 
    %s, t.Weight_lbs = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

#New Record page
@app.route('/biostats/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Profile')

# Update DB with new record.
@app.route('/biostats/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('Name'), request.form.get('Sex'), request.form.get('Age'), request.form.get('Height_in'), request.form.get('Weight_lbs'))
    sql_insert_query = """INSERT INTO biostatsImport (Name,Sex,Age,Height_in,Weight_lbs) VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

#Delete Record
@app.route('/delete/<int:biostats_id>', methods=['POST'])
def form_delete_post(biostats_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM biostatsImport WHERE id = %s """
    cursor.execute(sql_delete_query, biostats_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/biostats', methods=['GET'])
def api_browse() -> Response:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostatsImport')
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/biostats/<int:biostats_id>', methods=['GET'])
def api_retrieve(biostats_id) -> Response:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM biostatsImport WHERE id=%s', biostats_id)
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp

#This will add a record to the JSON Database
@app.route('/api/v1/biostats', methods=['POST'])
def api_add() -> Response:
    content = request.json
    cursor = mysql.get_db().cursor()
    inputData = (content['Name'], content['Sex'], content['Age'], content['Height_in'], request.form.get('Weight_lbs'))
    sql_insert_query = """INSERT INTO biostatsImport (Name,Sex,Age,Height_in,Weight_lbs) VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp

#This will allow edits to a record and update the JSON Database.
@app.route('/api/v1/biostats/<int:biostats_id>', methods=['PUT'])
def api_edit(biostats_id) -> Response:
    cursor = mysql.get_db().cursor()
    content = request.json
    inputData = (content['Name'], content['Sex'], content['Age'], content['Height_in'], content['Weight_lbs'], biostats_id)
    sql_update_query = """UPDATE biostatsImport t SET t.Name = %s, t.Sex = %s, t.Age = %s, t.Height_in = %s, t.Weight_lbs = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp

#This will delete a record and update the JSON Database.
@app.route('/api/v1/biostats/<int:biostats_id>', methods=['DELETE'])
def api_delete(biostats_id) -> Response:
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM biostatsImport WHERE id = %s """
    cursor.execute(sql_delete_query, biostats_id)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp

#Forms
@app.route("/biostats/contact", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.html",
        form=form,
        template="form-template"
    )

@app.route("/biostats/signup", methods=["GET", "POST"])
def signup():
    """User sign-up form for account creation."""
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "signup.html",
        form=form,
        template="form-template",
        title="Signup Form"
    )

@app.route("/biostats/success", methods=["GET", "POST"])
def success():
    """Generic success page upon form submission."""
    return render_template(
        "success.html",
        template="success-template"
    )

#Error Handling
@app.errorhandler(404)
def not_found():
    """Page not found."""
    return Response(render_template("404Error.html"), 404)

@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return Response(render_template("400Error.html"), 400)


@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return Response(render_template("500Error.html"),500)

@app.route("/biostats/users", methods=["GET"])
def user_records():
    """Create a user via query string parameters."""
    username = request.args.get("user")
    email = request.args.get("email")
    if username and email:
        existing_user = User.query.filter(
            User.username == username or User.email == email
        ).first()
        if existing_user:
            return make_response(f"{username} ({email}) already created!")
        new_user = User(
            username=username,
            email=email,
            created=dt.now(),
            bio="In West Philadelphia born and raised, \
            on the playground is where I spent most of my days",
            admin=False,
        )  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        redirect(url_for("user_records"))
    return render_template("users.html", users=User.query.all(), title="Show Users")

@app.route('/', methods=['GET'])
def create_user():
    """Create a user."""
    ...
    return render_template(
        'users.html',
        users=User.query.all(),
        title="Show Users"
    )