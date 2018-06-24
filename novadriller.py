from flask import Flask, render_template,request, redirect, url_for
import time, serial

app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) #Open serial port
print ('Serial connection to Arduino initialized on',ser.name)

# variables for template page (templates/driller.html)
author = "Neil Isenor"
LEDOn = 0
driveD = 0
driveS = 1000
driveT = 0
drillX = 0
drillZ = 0
drillOn = 0


# we are able to make 2 different requests on our webpage
# GET = we just type in the url
# POST = some sort of form submission like a button
@app.route('/driller', methods = ['POST','GET'])
def drillerx():
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
            drillerSerial = "%s %s %s %s %s %s %s" % (LEDOn, driveD, driveS, driveT, drillX, drillZ, drillOn)

            # write serial values to driller
            ser.write(drillerSerial.encode())
            print (drillerSerial)

        elif request.form.get('led', False) == 'LED Off':
            print ('LED OFF')
            LEDOn = 0
            drillerSerial = "%s %s %s %s %s %s %s" % (LEDOn, driveD, driveS, driveT, drillX, drillZ, drillOn)

            # write serial values to driller
            ser.write(drillerSerial.encode())
            print (drillerSerial)

        elif request.form.get('drill', False) == 'Drill On':
            print ('DRILL ON')
            drillOn = 1
            drillerSerial = "%s %s %s %s %s %s %s" % (LEDOn, driveD, driveS, driveT, drillX, drillZ, drillOn)

            # write serial values to driller
            ser.write(drillerSerial.encode())
            print (drillerSerial)

        elif request.form.get('drill', False) == 'Drill Off':
            print ('DRILL OFF')
            drillOn = 0
            drillerSerial = "%s %s %s %s %s %s %s" % (LEDOn, driveD, driveS, driveT, drillX, drillZ, drillOn)

            # write serial values to driller
            ser.write(drillerSerial.encode())
            print (drillerSerial)

        # if we press the submit button
        elif request.form['submit'] == 'Submit':
            print ('SUBMIT')
            drillerSerial = "%s %s %s %s %s %s %s" % (LEDOn, driveD, driveS, driveT, drillX, drillZ, drillOn)

            # write serial values to driller
            ser.write(drillerSerial.encode())
            print (drillerSerial)


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
