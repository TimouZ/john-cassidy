#!usr/bin/env/ python
# coding: utf-8

from datetime import datetime
import io

from camera_pi import Camera
from flask import Flask
from flask import render_template

from helpers import generate_frame

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_stream')
def video_stream():
    return Response(generate_frame(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



