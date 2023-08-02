# -*- coding: utf-8 -*-
"""
Created on Fri May 19 20:38:20 2023

@author: Arunagiri.S.S
"""

from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello'

app.run(debug=True   )