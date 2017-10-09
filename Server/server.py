# -*- coding: UTF-8 -*-
from os import abort

from flask import Flask, jsonify, render_template, request, url_for  # From module flask import class Flask

from Database.database import db_session, init_db
from Database.models import User

app = Flask(__name__)  # Construct an instance of Flask class for our webapp


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def main():
    """Render an HTML template and return"""
    return render_template('hello.html')  # HTML file to be placed under sub-directory templates


@app.route('/sismic/registration_form')
def test():
    """Render an HTML template and return"""
    if request.method == 'GET': return render_template('hello.html')
    email = request.args.get['email']
    password = request.args.get['secret']
    name = request.args.get['name']
    address = request.args.get['address']
    phone = request.args.get['phone']
    qualification = request.args.get['qualification']
    register = request.args.get['register']
    if email is None or password is None:
        abort(400)  # missing arguments
    if User.query.filter_by(username=email).first() is not None:
        abort(400)  # existing user

    user = User(email, password, name, address, phone, qualification, register)
    db_session.add(user)
    db_session.commit()
    return jsonify({'username': user.username}), 201, {'Location': url_for('get_user', id=user.id, _external=True)}


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='192.168.0.2', port=5000)  # Launch built-in web server and run this Flask webapp


@app.route('/sismic/registration_form')
def handle_registration():
    if request.method == 'GET': return render_template('hello.html')
    email = request.args.get['email']
    password = request.args.get['secret']
    name = request.args.get['name']
    address = request.args.get['address']
    phone = request.args.get['phone']
    qualification = request.args.get['qualification']
    register = request.args.get['register']
    if email is None or password is None:
        abort(400)  # missing arguments
    if User.query.filter_by(username=email).first() is not None:
        abort(400)  # existing user

    user = User(email, password, name, address, phone, qualification, register)
    db_session.add(user)
    db_session.commit()
    return jsonify({'username': user.username}), 201, {'Location': url_for('get_user', id=user.id, _external=True)}


@app.route('/sismic/login_form')
def handle_login():
    username = request.args.get['username']
    password = request.args.get['secret']
    user = User.query.filter_by(username=username).first()
    if not user:
        abort(400)
    else:
        if user.verify_password(password):
            return jsonify({'username': user.username}), 201, {
                'Location': url_for('get_user', id=user.id, _external=True)}
        else:
            abort(400)


@app.route('/sismic/reports', methods=["GET"])
def show_reports():
    pass


@app.route('/sismic/upload_report', methods=["POST"])
def upload_report():
    pass


@app.route('/sismic/upload_report_files', methods=["POST"])
def upload_file():
    pass
