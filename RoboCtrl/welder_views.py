from flask import Flask, render_template, request, redirect, url_for, Blueprint
from RoboCtrl import app
from RoboCtrl.views import *
import time, serial

welder_views = Blueprint('welder_views', __name__,
                        template_folder='templates')

# variables for template page (welder.html)
arm_select = 0
theta_target = 0
r_target = 0
arm_speed_target = 20
left_z = 0
right_z = 0
wire_speed = 0
distance = 0
speed = 1000
trim = 0
argon = 0
outriggers = 0
led = 0
click_pos = None
author = "Neil Isenor"

@welder_views.route('/welder', methods = ['POST','GET'])
def welderx():

    def buildSerial():
        try:
            welderSerial = "%s %s %s %s %s %s %s %s %s %s %s %s" % (arm_select, theta_target, r_target, arm_speed_target, left_z, right_z, wire_speed, distance, speed, trim, argon, outriggers, led)
            # write serial values to welder
            # ser.write(welderSerial.encode())
            print (welderSerial)
            f = open("/tmp/welder/rw_arm_select", "w+")
            f.write(str(arm_select))
            f = open("/tmp/welder/rw_theta_target", "w+")
            f.write(str(theta_target))
            f = open("/tmp/welder/rw_r_target", "w+")
            f.write(str(r_target))
            f = open("/tmp/welder/rw_arm_speed_target", "w+")
            f.write(str(arm_speed_target))
            f = open("/tmp/welder/rw_left_z", "w+")
            f.write(str(left_z))
            f = open("/tmp/welder/rw_right_z", "w+")
            f.write(str(arm_select))
            f = open("/tmp/welder/rw_distance", "w+")
            f.write(str(distance))
            f = open("/tmp/welder/rw_speed", "w+")
            f.write(str(speed))
            f = open("/tmp/welder/rw_trim", "w+")
            f.write(str(trim))
            f = open("/tmp/welder/rw_wire_speed", "w+")
            f.write(str(wire_speed))
            f = open("/tmp/welder/rw_argon", "w+")
            f.write(str(argon))
            f = open("/tmp/welder/rw_outriggers", "w+")
            f.write(str(outriggers))
            f = open("/tmp/welder/rw_led", "w+")
            f.write(str(led))
        except IOError as e:
            print("ERROR: OPERATION FAILED")

    global arm_select, theta_target, r_target, arm_speed_target, left_z, right_z, distance, speed, trim, wire_speed, argon, outriggers, led
    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':

        theta_target = request.form['theta_target']
        r_target = request.form['r_target']
        arm_speed_target = request.form['arm_speed_target']
        left_z = request.form['left_z']
        right_z = request.form['right_z']
        wire_speed = request.form['wire_speed']
        distance = request.form['distance']
        speed = request.form['speed']
        trim = request.form['trim']

        if request.form.get('argon', 0) == 'Argon On':
            print ('ARGON ON')
            argon = 1
            buildSerial()

        elif request.form.get('argon', 0) == 'Argon Off':
            print ('ARGON OFF')
            argon = 0
            buildSerial()

        elif request.form.get('arm', 0) == 'Welding Arm':
            print ('WELDING ARM')
            arm_select = 0
            buildSerial()

        elif request.form.get('arm', 0) == 'Grinding Arm':
            print ('GRINDING ARM')
            arm_select = 1
            buildSerial()

        elif request.form.get('outriggers', 0) == 'Outriggers On':
            print ('outriggers ON')
            outriggers = 1
            buildSerial()

        elif request.form.get('outriggers', 0) == 'Outriggers Off':
            print ('outriggers OFF')
            outriggers = 0
            buildSerial()

        elif request.form.get('led', 0) == 'Left LED On':
            print ('LEFT LED ON')
            led = 1
            buildSerial()

        elif request.form.get('led', 0) == 'Right LED On':
            print ('RIGHT LED ON')
            led = 2
            buildSerial()

        elif request.form.get('led', 0) == 'Both LEDs On':
            print ('BOTH LEDS ON')
            led = 3
            buildSerial()


        elif request.form.get('led', 0) == 'Both LEDs Off':
            print ('BOTH LEDS OFF')
            led = 0
            buildSerial()

        # if we press the submit button
        elif request.form['submit'] == 'Submit':
            print ('SUBMIT')
            buildSerial()

        # if we press the reset all values button
        elif request.form['submit'] == 'Reset All Values':
            print ('RESET')

            # serial value to return to abs 0 positions
            arm_select = 0
            theta_target = 0
            r_target = 0
            arm_speed_target = 20
            left_z = 0
            right_z = 0
            wire_speed = 0
            distance = 0
            speed = 1000
            trim = 0
            argon = 0
            welder = 0
            led = 0
            outriggers = 0

        else:
            pass



    # the default page to display will be our template with our template variables
    return render_template('welder.html', author=author, arm_select=arm_select, theta_target=theta_target, r_target=r_target, arm_speed_target=arm_speed_target, left_z=left_z, right_z=right_z, wire_speed=wire_speed, distance=distance, speed=speed, trim=trim, argon=argon, led=led, outriggers=outriggers, localip=localip)
