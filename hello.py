#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:31:05 2020

@author: rajat
"""


from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['POST'])

def index():
    some_json = request.get_json()
    return jsonify({"sent": some_json})

@app.route('/multi/<int:num>', methods=['GET'])

def multiply(num):
    return jsonify({"result": num*100})

if __name__ == '__main__':
    app.run(debug=True)