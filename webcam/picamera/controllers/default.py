# -*- coding: utf-8 -*-
# BSD license.
# Massimo di Pierro and Luca de Alfaro, 2016.
# Simple web cam app for web2py.


import base64
import json
import os
import subprocess

def index():
    return dict()

PATH = '/ramfs/qr.jpg'

def picamera():
    filename = PATH
    with open(filename) as imagefile:
        try:
            image = imagefile.read()
            data = {'src':'data:image/jpeg;base64,'+base64.b64encode(image)}
        return json.dumps(data)


