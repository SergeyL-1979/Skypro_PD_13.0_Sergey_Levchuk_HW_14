#!/usr/bin/env python
# -*- coding: utf-8 -*-
# app.py
from flask import Flask
from blueprint import movies


app = Flask(__name__)
app.register_blueprint(movies)
