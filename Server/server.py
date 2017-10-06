# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask, jsonify, render_template  # From module flask import class Flask
from Database.database import db_session, init_db


app = Flask(__name__)  # Construct an instance of Flask class for our webapp


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def main():
    """Render an HTML template and return"""
    return render_template('hello.html')  # HTML file to be placed under sub-directory templates


if __name__ == '__main__':  # Script executed directly?
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)  # Launch built-in web server and run this Flask webapp


@app.route('/')
def a():
    return jsonify({'message': 'unknown user'}), 400
    # response.data is:
    # {
    #   "message": "unknown user"
    # }
