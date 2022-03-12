#!/usr/bin/env python

from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.test import TestController

# CRUD operations
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'


app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
  return "Utilities Tracker homepage"


@app.route('/test', methods=(GET, ))
def test():
    if request.method == 'GET':
        return TestController().getTest()
    return jsonify("Method not allowed"), 405

if __name__ == '__main__':
    app.run(debug=True) #go to http://utilities-tracker.herokuapp.com/ to view the app.