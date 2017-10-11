# -*- coding: UTF-8 -*-
from os import abort

from flask import Flask, jsonify, render_template, request, url_for  # From module flask import class Flask
from flask import make_response

from Database.database import db_session, init_db
from Database.models import User

app = Flask(__name__)  # Construct an instance of Flask class for our webapp


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/sismic/registration_form', methods=['POST'])
def handle_registration():
    email = request.args.get('email')
    password = request.args.get('secret')
    name = request.args.get('name')
    address = request.args.get('address')
    phone = request.args.get('phone')
    qualification = request.args.get('qualification')
    register = request.args.get('register')
    if email is None or password is None:
        make_response("", 560)  # missing arguments
    if User.query.filter_by(email=email).first() is not None:
        make_response("", 561)  # existing user

    user = User(email, password, name, address, phone, qualification, register)
    db_session.add(user)
    db_session.commit()
    return make_response("success", 200)


@app.route('/sismic/login_form', methods=['POST'])
def handle_login():
    email = request.args.get('email')
    password = request.args.get('secret')
    user = User.query.filter_by(email=email).first()
    if not user:
        return make_response("user not present", 550)
    else:
        if user.verify_password(password):
            response = jsonify(user.toDict())
            response.status_code = 200
            return response
        else:
            return make_response("invalid psw", 551)


@app.route('/sismic/reports', methods=["GET"])
def show_reports():
    pass


@app.route('/sismic/upload_report', methods=["POST"])
def upload_report():
    return jsonify(request)


@app.route('/sismic/upload_report_files', methods=["POST"])
def upload_file():
    pass


@app.route('/')
def main():
    """Render an HTML template and return"""
    return render_template('hello.html')  # HTML file to be placed under sub-directory templates


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='192.168.0.11', port=5000)  # Launch built-in web server and run this Flask webapp
