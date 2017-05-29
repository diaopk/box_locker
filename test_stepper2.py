# This script provides stepper motor control
# to turn the xxx
# using RPI.GPIO library

# Import required modules
import RPI.GPIO as GPIO
from time import sleep

# Define a Motor class to control stepper motor
# --- Start of the class ---
class Motor:
    def __init__(self, pin1, pin2, pin3, pin4):
        GPIO.setmode(GPIO.BOARD)
        
        # Set pins
        self.pins = [pin1, pin2, pin3, pin4]
        
        # Set all pins as output
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

        # Define an advanced sequence
        self.seq = [[1,0,0,1],
                [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1]]

        self.seq1 = [[1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1],
                [1,0,0,1]]

        self.seq1_reverse = [[1,0,0,1],
                [0,0,0,1],
                [0,0,1,1],
                [0,0,1,0],
                [0,1,1,0],
                [0,1,0,0],
                [1,1,0,0],
                [1,0,0,0]]

        self.seq2 = [[1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]]

        self.seq2_reverse = [[1,0,0,0],
                [0,0,0,1],
                [0,0,1,0],
                [0,1,0,0]]

        self.step_count = len(self.seq)
        # Set to 1 or 2 for clockwise
        # Set to -1 or -2 for anti-clockwise
        self.step_add = 1
        self.step_counter = 0

        # Define the wait time
        self.waittime = 0.00001

    # Method to set attributes
    def set_waittime(self, t): self.waittime = t
    def set_step_add(self, a): self.step_add = a

    # Method to turn 90 deg
    def open(self):
        print self.step_counter
        print self.seq[self.step_counter]

        for i in range(0, 512/4):
        for p in range(0, 4):
            pin_on_board = self.seq[p]
            if self.seq[self.step_counter][p] == 1:
                print "Enable pin %i" % (pin_on_board)
                GPIO.output(pin_on_board, 1)
            else:
                GPIO.output(pin_on_board, 0)

        self.step_counter += self.step_add

        # If it rearches the end of the sequence
        # start again
        if self.step_counter >= self.step_count:
            self.step_counter = 0

        sleep(self.waittime)

    # Reset the pins
    GPIO.cleanup()

    # Method to turn back 90 deg
    def close(self):
        print self.step_conuter
        print self.seq[self.step_counter]

        for i in range(0, 128):
            for p in range(0,4):
                pin_on_board = self.seq[p]
                if self.seq[self.step_counter][p] == 1:
                    print "Enable pin %i" % (pin_on_board)
                    GPIO.output(pin_on_board, 1)
                else:
                    GPIO.output(pin_on_board, 0)

            self.step_counter += self.step_add

            # If it rearches the end of the sequence
            # start agagin
            if self.step_counter >= self.step_count:
                self.step_counter = 0

            sleep(self.waittime)

        # Reset the pins
        GPIO.cleanup()
            
# --- End of the class ---
