from flask import Flask, render_template, request, redirect, url_for, Blueprint
from RoboCtrl import app
import time, serial, json

views = Blueprint('views', __name__,
                        template_folder='templates')
"""
try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) #Open serial port
    print ('Serial connection to Arduino initialized on',ser.name)
except IOError as e:
    print ('SERIAL CONNECTION COULD NOT BE MADE, CHECK CONNECTION AND RERUN THE APPLICATION')
"""

@views.route('/')
def index():
    return 'Use /driller or /welder'

@views.route('/click_pos', methods = ['POST','GET'])
def click_pos():
    x = request.args.get('x', 0, type=int)
    y = request.args.get('y', 0, type=int)
    width = request.args.get('width', 0, type=int)
    height = request.args.get('height', 0, type=int)
    percent_x = request.args.get('percent_x', 0, type=float)
    percent_y = request.args.get('percent_y', 0, type=float)
    f = open("/tmp/click_pos.tmp", "w+")
    f.write(str(x) + ", " + str(y) + ", " + str(width) + ", " + str(height) + ", " + str(percent_x) + ", " + str(percent_y))
    return 'OK'

if __name__ == "__main__":

    # lets launch our webpage!
    # do 0.0.0.0 so that we can log into this webpage
    # using another computer on the same network later
    app.run(host='0.0.0.0')
