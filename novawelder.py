from flask import Flask, render_template,request, redirect, url_for
import time, serial

app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) #Open serial port
print ('Serial connection to Arduino initialized on',ser.name)

# variables for template page (welder.html)
left_theta_target = 0
left_r_target = 0
left_z = 0
right_theta_target = 0
right_r_target = 0
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

    global left_theta_target, left_r_target, left_z, right_theta_target, right_r_target, right_z, distance, speed, trim, wire_speed, argon, welder, air, led
    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':

        left_theta_target = request.form['left_theta_target']
        left_r_target = request.form['left_r_target']
        left_z = request.form['left_z']
        right_theta_target = request.form['right_theta_target']
        right_r_target = request.form['right_r_target']
        right_z = request.form['right_z']
        wire_speed = request.form['wire_speed']
        distance = request.form['distance']
        speed = request.form['speed']
        trim = request.form['trim']


        if request.form.get('argon', False) == 'Argon On':
            print ('ARGON ON')
            argon = 1
            welderSerial = "%s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (left_theta_target, left_r_target, left_z, right_theta_target, right_r_target, right_z, wire_speed, distance, speed, trim, argon, welder, air, led)

            # write serial values to welder
            ser.write(welderSerial.encode())
            print (welderSerial)

        elif request.form.get('argon', False) == 'Argon Off':
            print ('ARGON OFF')
            argon = 0
            welderSerial = "%s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (left_theta_target, left_r_target, left_z, right_theta_target, right_r_target, right_z, wire_speed, distance, speed, trim, argon, welder, air, led)

            # write serial values to welder
            ser.write(welderSerial.encode())
            print (welderSerial)

        elif request.form.get('welder', False) == 'Welder On':
            print ('WELDER ON')
            welder = 1
            welderSerial = "%s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (left_theta_target, left_r_target, left_z, right_theta_target, right_r_target, right_z, wire_speed, distance, speed, trim, argon, welder, air, led)

            # write serial values to welder
            ser.write(welderSerial.encode())
            print (welderSerial)

        elif request.form.get('welder', False) == 'Welder Off':
            print ('WELDER OFF')
            welder = 0
            welderSerial = "%s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (left_theta_target, left_r_target, left_z, right_theta_target, right_r_target, right_z, wire_speed, distance, speed, trim, argon, welder, air, led)

            # write serial values to welder
            ser.write(welderSerial.encode())
            print (welderSerial)

        elif request.form.get('air', False) == 'Air On':
            print ('AIR ON')
            air = 1
            welderSerial = "%s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (left_theta_target, left_r_target, left_z, right_theta_target, right_r_target, right_z, wire_speed, distance, speed, trim, argon, welder, air, led)

            # write serial values to welder
            ser.write(welderSerial.encode())
            print (welderSerial)

        elif request.form.get('air', False) == 'Air Off':
            print ('AIR OFF')
            air = 0
            welderSerial = "%s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (left_theta_target, left_r_target, left_z, right_theta_target, right_r_target, right_z, wire_speed, distance, speed, trim, argon, welder, air, led)
            # write serial values to welder
            ser.write(welderSerial.encode())
            print (welderSerial)

        elif request.form.get('led', False) == 'Right LED On':
            print ('RIGHT LED ON')
            led = 1
            welderSerial = "%s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (left_theta_target, left_r_target, left_z, right_theta_target, right_r_target, right_z, wire_speed, distance, speed, trim, argon, welder, air, led)
            # write serial values to welder
            ser.write(welderSerial.encode())
            print (welderSerial)

        elif request.form.get('led', False) == 'Left LED On':
            print ('LEFT LED ON')
            led = 2
            welderSerial = "%s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (left_theta_target, left_r_target, left_z, right_theta_target, right_r_target, right_z, wire_speed, distance, speed, trim, argon, welder, air, led)

            # write serial values to welder
            ser.write(welderSerial.encode())
            print (welderSerial)


        elif request.form.get('led', False) == 'Both LEDs On':
            print ('BOTH LEDS ON')
            led = 3
            welderSerial = "%s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (left_theta_target, left_r_target, left_z, right_theta_target, right_r_target, right_z, wire_speed, distance, speed, trim, argon, welder, air, led)

            # write serial values to welder
            ser.write(welderSerial.encode())
            print (welderSerial)


        elif request.form.get('led', False) == 'Both LEDs Off':
            print ('BOTH LEDS OFF')
            led = 0
            welderSerial = "%s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (left_theta_target, left_r_target, left_z, right_theta_target, right_r_target, right_z, wire_speed, distance, speed, trim, argon, welder, air, led)

            # write serial values to welder
            ser.write(welderSerial.encode())
            print (welderSerial)

        # if we press the submit button
        elif request.form['submit'] == 'Submit':
            print ('SUBMIT')
            welderSerial = "%s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (left_theta_target, left_r_target, left_z, right_theta_target, right_r_target, right_z, wire_speed, distance, speed, trim, argon, welder, air, led)

            # write serial values to welder
            ser.write(welderSerial.encode())
            print (welderSerial)

        # if we press the reset all values button
        elif request.form['submit'] == 'Reset All Values':
            print ('RESET')

            # serial value to return to abs 0 positions
            left_theta_target = 0
            left_r_target = 0
            left_z = 0
            right_theta_target = 0
            right_r_target = 0
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
    return render_template('welder.html', author=author, left_theta_target=left_theta_target, left_r_target=left_r_target, left_z=left_z, right_theta_target=right_theta_target, right_r_target=right_r_target, right_z=right_z, wire_speed=wire_speed, distance=distance, speed=speed, trim=trim, argon=argon, welder=welder, led=led, air=air)

if __name__ == "__main__":

    # lets launch our webpage!
    # do 0.0.0.0 so that we can log into this webpage
    # using another computer on the same network later
    app.run(host='0.0.0.0')
