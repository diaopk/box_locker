#!/usr/...
# This script is the header containing some functions that are needed and 
# invoked in the xxx.py

# Import picamera python module
from picamera import *
import datetime

# Variables
camera = PiCamera()

# A Method to take a photo
def photor1():
    camera.capture('./test_picamera/image-'+str(datetime.datetime.now())+'.jpg')
    print 'Sorry we captured you!'

# Object photor
class Photor():
    def __init__(self, p, d):
        self.path = p
        self.datetime = d

    def take_photo():
        camera.capture('./test_picamera/-'+str(self.datetime)+'.jpg')
        print 'Sorry we captured you!'

    def get_datetime():
        return self.get_datetime


