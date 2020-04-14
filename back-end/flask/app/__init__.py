# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:42:35 2020

@author: iurym
"""
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow cross origin references
cors = CORS(app, resources={r"/predict/*": {"origins": "*"}})

from app import views