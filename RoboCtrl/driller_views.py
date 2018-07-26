from flask import Flask, render_template, request, redirect, url_for, Blueprint
from RoboCtrl import app
from RoboCtrl.views import *
import time, serial

driller_views = Blueprint('driller_views', __name__,
                        template_folder='templates')

# variables for template page (templates/driller.html)
author = "Neil Isenor"
led = 0
distance = 0
speed = 1000
trim = 0
drill_x_position = 0
drill_depth = 0
drill_enable = 0

@driller_views.route('/driller', methods = ['POST','GET'])
def drillerx():

    def buildSerial():
        try:
            drillerSerial = "%s %s %s %s %s %s %s" % (led, distance, speed, trim, drill_x_position, drill_depth, drill_enable)
            # write serial values to driller
            # ser.write(drillerSerial.encode())
            print (drillerSerial)
            f = open("/tmp/dled.tmp", "w+")
            f.write(str(led))
            f = open("/tmp/ddistance.tmp", "w+")
            f.write(str(distance))
            f = open("/tmp/dspeed.tmp", "w+")
            f.write(str(speed))
            f = open("/tmp/dtrim.tmp", "w+")
            f.write(str(trim))
            f = open("/tmp/drill_x_position.tmp", "w+")
            f.write(str(drill_x_position))
            f = open("/tmp/drill_depth", "w+")
            f.write(str(drill_depth))
            f = open("/tmp/drill_enable.tmp", "w+")
            f.write(str(drill_enable))
        except NameError as e:
            print("ERROR: OPERATION FAILED")


    global led, distance, speed, trim, drill_x_position, drill_depth, drill_enable

    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':

        distance = request.form['distance']
        speed = request.form['speed']
        trim = request.form['trim']
        drill_x_position = request.form['drill_x_position']
        drill_depth = request.form['drill_depth']
        drillerSerial = "%s %s %s %s %s %s %s" % (led, distance, speed, trim, drill_x_position, drill_depth, drill_enable)

        if request.form.get('led', 0) == 'LED On':
            print ('LED ON')
            led = 1
            buildSerial()

        elif request.form.get('led', 0) == 'LED Off':
            print ('LED OFF')
            led = 0
            buildSerial()

        elif request.form.get('drill', 0) == 'Drill On':
            print ('DRILL ON')
            drill_enable = 1
            buildSerial()

        elif request.form.get('drill', 0) == 'Drill Off':
            print ('DRILL OFF')
            drill_enable = 0
            buildSerial()

        # if we press the submit button
        elif request.form['submit'] == 'Submit':
            print ('SUBMIT')
            buildSerial()

        # if we press the reset all values button
        elif request.form['submit'] == 'Reset All Values':
            print ('RESET')

            # serial value to return to abs 0 positions
            led = 0
            distance = 0
            speed = 1000
            trim = 0
            drill_x_position = 0
            drill_depth = 0
            drill_enable = 0

        else:
            pass

    # the default page to display will be our template with our template variables
    return render_template('driller.html', author=author, led=led, distance=distance, speed=speed, trim=trim, drill_x_position=drill_x_position, drill_depth=drill_depth, drill_enable=drill_enable)
