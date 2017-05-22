#!/usr/...
# This script defines a Photo Manager that implements the iterator protocol
# to store and orgnise photos
# ,and a Photo object

# Import required modules
from picamera import *
from datetime import datetime
from os import listdir
from re import search

# Photo Manager
class Photo_Manager:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution(800,480)
        self.photo_seq = self.__browse() # photo_seq holds a sequence of photo objects
        self.index = 0 # index hold the current index of a photo object
        self.current_photo = self.photo_seq[self.index] # current photo object

    def __iter__(self): return self
    def get_photos(self): return self.photo_seq
    def get_current_photo(self): return self.current_photo
    def get_index(self): return self.index

    # Method to take photo and store it into the photo_seq
    def take_photo(self):
        time = datetime.now()
        path = './test_picamera/%s.jpg' % time
        self.camera.capture(path)
        photo = Photo(path, time)
        self.photo_seq.append(photo)
        self.current_photo = self.photo_seq[0]

    # Method to list all photos in the directory
    # and store them as photo objects into photo_seq
    def __browse(self):
        lst = listdir('./test_picamera/')
        res_lst = []
        for photo in lst:
            if search('.jpg$', str(photo)):
                path = './test_picamera/' + str(photo)
                time = photo.partition('.jpg')[0]
                res_lst.append(Photo(path, time))
            elif search('.png$', str(photo)):
                path = './test_picamera/' + str(photo)
                time = photo.partition('.png')[0]
                res_lst.append(Photo(path, time))

        return res_lst

    # Method to return next photo object
    # and set index and current_photo to the next photo object
    def next(self):
        """try:
            self.index += 1
            self.current_photo = self.photo_seq[self.index].get_path()
            return self.photo_seq[self.index]
        except StopIteration, e:
            print 'stop', e
            #pass
            return None"""
        if self.index < len(self.photo_seq) -1: 
            self.index += 1
            self.current_photo = self.photo_seq[self.index]
            return self.photo_seq[self.index]
        else:
            print 'stop'
            raise

    
    # Method to return previous photo object
    # and set index and current_photo to the previous photo object
    def up(self):
        try:
            self.index -= 1
            self.current_photo = self.photo_seq[self.index]
        except StopIteration, e:
            print 'stop', e
            pass
        return self.photo_seq[self.index]
    
    # Method to return the first photo object of the photo_seq
    # and set index and current_photo to the first photo object
    def first(self):
        if len(self.photo_seq) >= 1:
            self.refresh()
            return self.photo_seq[0]
        else:
            print 'empty photo_seq'
            pass
    
    # Method to return the last photo object of the phpoto_seq
    # and set index and current_photo to the last photo object
    def last(self):
        if len(self.photo_seq) == 1:
            self.refresh()
            return self.photo_seq[0]
        elif len(self.photo_seq) > 1:
            self.index = len(self.photo_seq) - 1 
            self.current_photo = self.photo_seq[len(self.photo_seq)-1]
            return self.photo_seq[len(self.photo_seq)-1]
        else:
            print 'Empty photo_seq'
            pass

    # Method to make current photo back to the origional state
    # and set index and current_photo to the first photo object
    def refresh(self):
        if len(self.photo_seq) == 0:
            pass
        else:
            self.index = 0
            self.current_photo = self.photo_seq[0]

# Photo object
class Photo:
    def __init__(self, path, datetime):
        self.path = path
        self.datetime = datetime

    def get_datetime(self): return self.datetime
    def get_path(self): return self.path
