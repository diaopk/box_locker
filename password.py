#!/usr/...
# This script defines a pin object and relevant methods with it

# Import required modules and libraries
from uuid import uuid4
from hashlib import sha1

class Pin():
    def __init__(self):
        self.__pin = 1234
        self.__salt = self.__salt_create()

    # Method to create the salt
    def __salt_create(self):
        salt = uuid4().hex
        return salt
    
    # Method to create a hashed password
    def pin_create(self, pswd=None):
        if pswd is not None:
            return sha1(self.__salt.encode() + str(pswd).encode()).hexdigest() + ":" + self.__salt
        else:
            return sha1(self.__salt.encode() + str(self.__pin).encode()).hexdigest() + ":" + self.__salt

    # Method to check the passwod
    def pin_check(self, hashed_pswd, input_pswd):
        password, salt = self.pin_create(self.__pin).split(':')
        return password == sha1(salt.encode() + str(input_pswd).encode()).hexdigest()
