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
class Photo():
    def __init__(self):
        self.datetime, self.path = self.take_photo()

    def take_photo(self):
        time = datetime.datetime.now()
        path = './test_picamera/'+str(time)+'.jpg'
        camera.capture(path)
        print 'Sorry we captured you!'
        return (time, path)

    def get_datetime(self):
        return self.datetime

