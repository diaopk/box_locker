#!/usr/...
# This script is the header containing some functions that are needed and 
# invoked in the xxx.py

# Import picamera python module
from picamera import *
import datetime

# Variables
camera = PiCamera()

# A Method to take a photo
def photor():
    camera.capture('./test_picamera/image-'+str(datetime.datetime.now())+'.jpg')
    print 'Sorry we captured you!'

