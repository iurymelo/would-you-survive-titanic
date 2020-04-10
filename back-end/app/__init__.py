# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:42:35 2020

@author: iurym
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

from app import views