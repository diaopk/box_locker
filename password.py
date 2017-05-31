#!/usr/...
# This script defines a pin object and relevant methods with it

# Import required modules and libraries
from uuid import uuid4
from hashlib import sha1
from random import randint
from Emailer import Email

class Pin():
    def __init__(self):
        self.__pin = 1234
        self.__salt = self.__salt_create()

    # Method to create the salt
    def __salt_create(self):
        salt = uuid4().hex
        return salt
    
    # Method to crete a new pin
    # generate a 4-digit random number
    # and send it through emails
    def pin_forget(self):
        self.__pin = randint(1000, 9999) 
        self.__salt = self. __salt_create()
        server = Email()
        body = 'The pin has changed to %s' % (str(self.__pin))
        server.send(to_addr=server.to_addr_junli, body=body)
        server.send(to_addr=server.to_addr_caroline, body=body)
        server.send(to_addr=server.to_addr_louise, body=body)
    
    # Method to create a hashed password
    def pin_create(self, pswd=None, change=None):
        if pswd is not None and change == True:
            self.__pin = pswd
            self.__salt = self.__salt_create()
            server = Email()
            body = 'The pin has been changed to %s' % (str(self.__pin))
            server.send(to_addr=server.to_addr_junli, body=body)
            server.send(to_addr=server.to_addr_caroline, body=body)
            server.send(to_addr=server.to_addr_louise, body=body)

        return sha1(self.__salt.encode() + str(self.__pin).encode()).hexdigest() + ":" + self.__salt

    # Method to check the passwod
    def pin_check(self, input_pswd):
        password, salt = self.pin_create(self.__pin).split(':')
        return password == sha1(salt.encode() + str(input_pswd).encode()).hexdigest()

# --- End of the class ---

