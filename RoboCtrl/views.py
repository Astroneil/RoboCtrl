from flask import Flask, render_template, request, redirect, url_for
from RoboCtrl import app
import time, serial, cv2

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) #Open serial port
print ('Serial connection to Arduino initialized on',ser.name)

#Detect Number of plugged-in Cameras - Broken until I can install OpenCV
def detectNumCameras(self):
    ind = 0
    while True:
        vc = cv2.VideoCapture(ind)
        if (vc.isOpened()):
            ind += 1
            vc.release()
        else:
            break
    return(ind)

@app.route('/')
def index():
    return 'Use /driller or /welder'

# variables for template page (welder.html)
arm_select = 0
r_target = 0
left_z = 0
theta_target = 0
right_z = 0
wire_speed = 0
distance = 0
speed = 1000
trim = 0
argon = 0
welder = 0
air = 0
led = 0
author = "Neil Isenor"

# we are able to make 2 different requests on our webpage
# GET = we just type in the url
# POST = some sort of form submission like a button
@app.route('/welder', methods = ['POST','GET'])
def welderx():

    def buildSerial():
        welderSerial = "%s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (arm_select, theta_target, r_target, left_z, right_z, wire_speed, distance, speed, trim, argon, welder, air, led)
        # write serial values to welder
        ser.write(welderSerial.encode())
        print (welderSerial)


    global arm_select, theta_target, r_target, left_z, right_z, distance, speed, trim, wire_speed, argon, welder, air, led
    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':

        theta_target = request.form['theta_target']
        r_target = request.form['r_target']
        left_z = request.form['left_z']
        right_z = request.form['right_z']
        wire_speed = request.form['wire_speed']
        distance = request.form['distance']
        speed = request.form['speed']
        trim = request.form['trim']


        if request.form.get('argon', False) == 'Argon On':
            print ('ARGON ON')
            argon = 1
            buildSerial()

        elif request.form.get('argon', False) == 'Argon Off':
            print ('ARGON OFF')
            argon = 0
            buildSerial()

        elif request.form.get('arm', False) == 'Welding Arm':
            print ('WELDING ARM')
            arm_select = 0
            buildSerial()

        elif request.form.get('argon', False) == 'Grinding Arm':
            print ('GRINDING ARM')
            arm_select = 1
            buildSerial()

        elif request.form.get('welder', False) == 'Welder On':
            print ('WELDER ON')
            welder = 1
            buildSerial()

        elif request.form.get('welder', False) == 'Welder Off':
            print ('WELDER OFF')
            welder = 0
            buildSerial()

        elif request.form.get('air', False) == 'Air On':
            print ('AIR ON')
            air = 1
            buildSerial()

        elif request.form.get('air', False) == 'Air Off':
            print ('AIR OFF')
            air = 0
            buildSerial()

        elif request.form.get('led', False) == 'Left LED On':
            print ('LEFT LED ON')
            led = 1
            buildSerial()

        elif request.form.get('led', False) == 'Right LED On':
            print ('RIGHT LED ON')
            led = 2
            buildSerial()

        elif request.form.get('led', False) == 'Both LEDs On':
            print ('BOTH LEDS ON')
            led = 3
            buildSerial()


        elif request.form.get('led', False) == 'Both LEDs Off':
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
            left_z = 0
            right_z = 0
            wire_speed = 0
            distance = 0
            speed = 1000
            trim = 0
            argon = 0
            welder = 0
            led = 0
            air = 0

        else:
            pass



    # the default page to display will be our template with our template variables
    return render_template('welder.html', author=author, arm_select=arm_select, theta_target=theta_target, r_target=r_target, left_z=left_z, right_z=right_z, wire_speed=wire_speed, distance=distance, speed=speed, trim=trim, argon=argon, welder=welder, led=led, air=air)

# variables for template page (templates/driller.html)
author = "Neil Isenor"
LEDOn = 0
driveD = 0
driveS = 1000
driveT = 0
drillX = 0
drillZ = 0
drillOn = 0

@app.route('/driller', methods = ['POST','GET'])
def drillerx():

    def buildSerial():
        drillerSerial = "%s %s %s %s %s %s %s" % (LEDOn, driveD, driveS, driveT, drillX, drillZ, drillOn)
        # write serial values to driller
        ser.write(drillerSerial.encode())
        print (drillerSerial)


    global LEDOn, driveD, driveS, driveT, drillX, drillZ, drillOn

    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':

        driveD = request.form['driveD']
        driveS = request.form['driveS']
        driveT = request.form['driveT']
        drillX = request.form['drillX']
        drillZ = request.form['drillZ']
        drillerSerial = "%s %s %s %s %s %s %s" % (LEDOn, driveD, driveS, driveT, drillX, drillZ, drillOn)


        if request.form.get('led', False) == 'LED On':
            print ('LED ON')
            LEDOn = 1
            buildSerial()

        elif request.form.get('led', False) == 'LED Off':
            print ('LED OFF')
            LEDOn = 0
            buildSerial()

        elif request.form.get('drill', False) == 'Drill On':
            print ('DRILL ON')
            drillOn = 1
            buildSerial()

        elif request.form.get('drill', False) == 'Drill Off':
            print ('DRILL OFF')
            drillOn = 0
            buildSerial()

        # if we press the submit button
        elif request.form['submit'] == 'Submit':
            print ('SUBMIT')
            buildSerial()


        # if we press the reset all values button
        elif request.form['submit'] == 'Reset All Values':
            print ('RESET')

            # serial value to return to abs 0 positions
            LEDOn = 0
            driveD = 0
            driveS = 1000
            driveT = 0
            drillX = 0
            drillZ = 0
            drillOn = 0

        else:
            pass

    # the default page to display will be our template with our template variables
    return render_template('driller.html', author=author, LEDOn=LEDOn, driveD=driveD, driveS=driveS, driveT=driveT, drillX=drillX, drillZ=drillZ, drillOn=drillOn)

if __name__ == "__main__":

    # lets launch our webpage!
    # do 0.0.0.0 so that we can log into this webpage
    # using another computer on the same network later
    app.run(host='0.0.0.0')
