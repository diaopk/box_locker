#!/usr/...
# This script for taking photoes if anyone try to access the box with
# the wrong pin
# This script basically defines some functions that are invoked in other
# scripts

# Import picamera python module
#import picamera as pc
from picamera import *
import datetime

# Variables
#camera = pc.PiCamera()
camera = PiCamera()

# A Method to take a photo
def photor():
    index = 0
    camera.capture('./test_picamera/image-'+str(datetime.datetime.now())+'.jpg')
    print 'Sorry we captured you!'

