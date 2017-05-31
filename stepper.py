# This script provides stepper motor control
# to turn the xxx
# using RPI.GPIO library

# Import required modules
import RPi.GPIO as GPIO
from time import sleep

# Define a Motor class to control stepper motor
# --- Start of the class ---
class Motor:
    def __init__(self):
        # Set pins
        self.pins = [36,35,38,37]
        
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
        self.waittime = 1/float(1000)

    # Method to set attributes
    def set_waittime(self, t): self.waittime = t
    def set_step_add(self, a): self.step_add = a

    # Method to turn 90 deg
    def open_test(self):
        print self.step_counter
        print self.seq[self.step_counter]

        while True:
            for p in range(0, 4):
                pin_on_board = self.seq[p]
                if self.seq[self.step_counter][p] != 0:
                    #print "Enable pin %d" % (pin_on_board)
                    GPIO.output(pin_on_board, True)
                else:
                    GPIO.output(pin_on_board, False)

            self.step_counter += self.step_add

        # If it rearches the end of the sequence
        # start again
            if self.step_counter >= self.step_count:
                self.step_counter = 0

            sleep(self.waittime)

    # Reset the pins
    #GPIO.cleanup()

    # Method to turn back 90 deg
    def open(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

        for i in range(0, 512*2):
            for pin in range(0,4):
                pin_on_board = self.pins[pin]
                if self.seq1_reverse[self.step_counter][pin] :
                    print "Enable pin %i" % (pin_on_board)
                    GPIO.output(pin_on_board, True)
                else:
                    GPIO.output(pin_on_board, False)

            self.step_counter += 1

            # If it rearches the end of the sequence
            # start agagin
            if self.step_counter >= self.step_count:
                self.step_counter = 0
            if self.step_counter < 0:
                self.step_counter = self.step_counter+self.step_add

            sleep(self.waittime)

        # Reset the pins
        GPIO.cleanup()
    
    # Method to turn 90 degree
    def close(self):
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)
        for i in range(0, 512*2):
            for pin in range(0,4):
                xpin=self.pins[pin]# Get GPIO
                
                if self.seq[self.step_counter][pin]!=0:
                    print " Enable GPIO %i" %(xpin)
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)
                
            self.step_counter += 1
                
            if (self.step_counter>=self.step_count):
                self.step_counter = 0
            if (self.step_counter<0):
                self.step_counter = self.step_count+self.step_add
                                                       
            sleep(self.waittime)

        GPIO.cleanup()
            
# --- End of the class ---
