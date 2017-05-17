#!/usr/...
# This script defines a pin object and relevant methods with it
# This is invoked in the xxx.py to generate a pin
from uuid import uuid4
from hashlib import sha1

class Pin():
    def __init__(self):
        self.pin
        self.salt

    def salt_create(self):
        return uuid4.hex()

    def pin_create(self, pswd):
        return sha1(self.salt_create().encode() + pswd.encode()).hexdiges()

