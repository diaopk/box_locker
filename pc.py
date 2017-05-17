#!/usr/...
# This script is the header containing some functions that are needed and 
# invoked in the xxx.py

# Import picamera python module
from picamera import *
import datetime

# Set up the camera variables
camera = PiCamera()
camera.resolution(800, 480)

# Object photor
class Photos():
    def __init__(self):
        self.datetime, self.path = self.take_photo()

    # Method to take a photo then return the datetime it take and its path
    def take_photo(self):
        time = datetime.datetime.now()
        path = './test_picamera/'+str(time)+'.jpg'
        camera.capture(path)
        print 'Sorry we captured you!'
        return (time, path)

    # Method to return the datetime
    def get_datetime(self): return self.datetime

    # Method to return path
    def get_path(self): return self.path

