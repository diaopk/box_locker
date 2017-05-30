#!/usr/bin/env python

# This code is written by Stephen C Phillips.
# It is in the public domain, so you can do what you like with it
# but a link to http://scphillips.com would be nice.

# It works on the Raspberry Pi computer with the standard Debian Wheezy OS and
# the 28BJY-48 stepper motor with ULN2003 control board.

# The motor seems to have 4096 positions(steps) it can point to. These don't 
# correspond exactly to degrees The class takes an angle we want the motor to point
# to, converts that into a step position and works out how many steps to turn it by
# and in waht direction to get there

# Actually, it does not move to the step position that is closest to the angle, it
# choose step position that are divisble by 8 because the control sequence has 8 step# in it

from time import sleep
import RPI.GPIO as GPIO

class Motor(object):
    def __init__(self, pins, mode=3):
        """Initialise the motor object.

        pins -- a list of 4 integers referring to the GPIO pins that the IN1, IN2
                IN3 and IN4 pins of the ULN2003 board are wired to
        mode -- the stepping mode to use:
                1: wave drive (not yet implemented)
                2: full step drive
                3: half step drive (default)

        """
        self.p1 = pins[0]
        self.p2 = pins[1]
        self.p3 = pins[2]
        self.p4 = pins[3]
        self.mode = mode

        # These stuff that i don't understand
        self.deg_per_step = 5.625 / 64 # For half-step drive (mode 3), means deg for each step
        self.steps_per_rev = int(360/self.deg_per_step)
        self.step_angle = 0 # Assume the way it is pointing is zero degrees

        for pin in pins:
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(pin, False)

    def _set_rpm(self, rpm):
        # Set the turn speed in RPM
        self._rpm = rpm
        # T is the amount of time to stop between signals
        self._T = (60.0/rpm) / self.steps_per_rev
    
    # This means you can set rpm as if it is an attributes and 
    # behind the scense it sets the _T attribute
    rpm = property(lambda self: self._rpm, _set_rpm)

    def move_to(self, angle):
        """ Take the shortest route to a particular angle (degrees). """
        # Make sure there is a 1:1 mapping between angle and stepper angle

        # angle/self.deg_per_step means how many steps needed
        # int(angle/self.deg_per_step) / 8 means 
        target_step_angle = 8 * (int(angle/self.deg_per_step)/8)
        steps = target_step_angle - self.step_angle
        steps = (steps % self.steps_per_rev)
        if steps > self.steps_per_rev /2:
            steps -= self.steps_per_rev
            print "moving " + 'steps' + " steps"
            if self.mode == 2:
                self._move_acw_2(-steps/8)
            else:
                self._move_acw_3(-steps/8)

        else:
            print "moveing " + 'steps' + " steps"
            if self.mode == 2:
                self._move_acw_2(steps/8)
            else:
                self._move_acw_3(steps/8)
        self.step_angle = target_step_angle

    def __clear(self):
        GPIO.output(self.p1, 0)
        GPIO.output(self.p2, 0)
        GPIO.output(self.p3, 0)
        GPIO.output(self.p4, 0)

    def _move_acw_2(self,big_steps):
        self.__clear()
        for i in range(big_steps):
            GPIO.output(self.p3, 0)
            GPIO.output(self.p1, 1)
            sleep(self._T * 2)
            GPIO.output(self.p2, 0)
            GPIO.output(self.p4, 1)
            sleep(self._T * 2)
            GPIO.output(self.P1, 0)
            GPIO.output(self.P3, 1)
            sleep(self._T * 2)
            GPIO.output(self.P4, 0)
            GPIO.output(self.P2, 1)
            sleep(self._T * 2) 
    
    def _move_acw_3(self, big_steps):
        self.__clear()
        for i in range(big_steps):
            GPIO.output(self.P1, 0)
            sleep(self._T)
            GPIO.output(self.P3, 1)
            sleep(self._T)
            GPIO.output(self.P4, 0)
            sleep(self._T)
            GPIO.output(self.P2, 1)
            sleep(self._T)
            GPIO.output(self.P3, 0)
            sleep(self._T)
            GPIO.output(self.P1, 1)
            sleep(self._T)
            GPIO.output(self.P2, 0)
            sleep(self._T)
            GPIO.output(self.P4, 1)
            sleep(self._T)

    def _move_cw_3(self, big_steps):
        self.__clear()
        for i in range(big_steps):
            GPIO.output(self.P3, 0)
            sleep(self._T)
            GPIO.output(self.P1, 1)
            sleep(self._T)
            GPIO.output(self.P4, 0)
            sleep(self._T)
            GPIO.output(self.P2, 1)
            sleep(self._T)
            GPIO.output(self.P1, 0)
            sleep(self._T)
            GPIO.output(self.P3, 1)
            sleep(self._T)
            GPIO.output(self.P2, 0)
            sleep(self._T)
            GPIO.output(self.P4, 1)
            sleep(self._T)

    # End of the class
