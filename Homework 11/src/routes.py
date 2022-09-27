from flask import render_template, request, flash, redirect, url_for, session, make_response
from werkzeug.utils import secure_filename
import pathlib
import uuid
from datetime import datetime, timedelta
from marshmallow import ValidationError
from flask_migrate import Migrate

from . import app, phonebook
from src.libs.validation_file import allowed_file
from src import users
from src.libs.validation_schemas import RegistrationSchema, LoginSchema


@app.before_request
def before_func():
    auth = True if 'username' in session else False
    if not auth:
        token_user = request.cookies.get('username')
        if token_user:
            user = users.get_user_by_token(token_user)
            if user:
                session['username'] = {"username": user.username, "id": user.id}


@app.route('/healthcheck')
def healthcheck():
    return 'I am working'


@app.route('/', strict_slashes=False)
def index():
    auth = True if 'username' in session else False
    return render_template('landing.html', title='Personal assistant!', auth=auth)


@app.route('/registration', methods=['GET', 'POST'], strict_slashes=False)
def registration():
    auth = True if 'username' in session else False
    if request.method == 'POST':
        try:
            RegistrationSchema().load(request.form)
        except ValidationError as err:
            return render_template('registration.html', messages=err.messages)
        email = request.form.get('email')
        password = request.form.get('password')
        nickname = request.form.get('nickname')
        user = users.create_user(email, password, nickname)
        return redirect(url_for('login'))
    if auth:
        return redirect(url_for('index'))
    else:
        return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    auth = True if 'username' in session else False
    print('auth')
    if request.method == 'POST':
        try:
            print('try')
            LoginSchema().load(request.form)
        except ValidationError as err:
            return render_template('login.html', messages=err.messages)

        email = request.form.get('email')
        password = request.form.get('password')
        user = users.login(email, password)

        if user is None:
            return redirect(url_for('login'))
        session['username'] = {"username": user.username, "id": user.id}
        response = make_response(redirect(url_for('main_table')))
        return response

    if auth:
        return redirect(url_for('main_table'))
    else:
        return render_template('login.html')


@app.route('/logout', strict_slashes=False)
def logout():
    auth = True if 'username' in session else False
    if not auth:
        return redirect(request.url)  # Відправляє туди звідки він прийшов
    session.pop('username')
    response = make_response(redirect(url_for('index')))
    response.set_cookie('username', '', expires=-1)

    return response


@app.route('/mainpage', methods=['GET', 'POST'], strict_slashes=False)
def main_table():
    auth = True if 'username' in session else False

    if request.method == 'POST' and request.form['submit'] == "Add":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        notes = request.form.get("notes")
        user_id = session['username']['id']
        users.create_contact(name, phone,email, notes, user_id)
        return redirect(url_for('main_table'))

    elif request.method == 'POST' and request.form['submit'] == "Delete":
        name = request.form.get("name")
        user_id = session['username']['id']
        users.delete_contact(name, user_id)
        return redirect(url_for('main_table'))

    elif request.method == 'POST' and request.form['submit'] == "Find":
        name = request.form.get("name")
        user_id = session['username']['id']
        user = users.find_contact(name, user_id)
        return render_template('find.html', auth=auth, users=user)

    else:

        if not auth:
            return redirect(request.url)
    #!!Write
        allcontacts = phonebook.get_phonebook_user(session['username']['id'])
        user_name = session['username']['username']

        contacts_amount = len(allcontacts)
        return render_template('mainpage.html', username=user_name, contacts_amount = contacts_amount, auth=auth, contacts = allcontacts)

    # Main page add






        #
        # # User ID from session data.
        # user_id = session.get("user_id")
        #
        # # Contact table id generation
        # table_id = 'user_' + str(session["user_id"]) + '_contacts'
        #
        # # Instantiating ContactTable and ContactTableManipulation classes.
        # # ContactSetUp = ContactTableSetUp(user_id, first_name, last_name, address, organization, number, email, social_handle, category)
        # # ContactManipulation = ContactTableManipulation(table_id,)
        #
        # # Handling different contact CRUD operations.....
        # # if update_contact == "Add Contact":
        #     # Inserting contact into table.
        #     # ContactSetUp.insert_contact()
        # # elif update_contact == "Update Contact":
        # # ContactManipulation.update_contact()
        #
        # # Updating sessions contact-list data.
        # # table_name = session["table_name"]
        # # user_contacts = ContactSetUp.return_all_contacts(table_name)
        # # session["user_contacts"] = user_contacts
        #
        # # End-points to be returned to main page.
        # # user_name = sess.get('user_name').title()
        # # contacts = sess["user_contacts"]
        # # contacts_amount = len(contacts)
        #
        # return render_template("mainPage.html", user_name=user_name, user_contacts=contacts, contacts_amount=contacts_amount)
