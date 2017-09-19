# CamJam Edukit 1 - Basics
# Worksheet 7 - Traffic Lights Template
# Import Libraries
import os
import time
from gpiozero import LED, Button, Buzzer

# Set pins 18, 23 and 24 to be LEDs .Set pin 25 as a button input
red = LED(18)
yellow = LED(23)
green = LED(24)

button = Button(25)
import os
import time
import RPi.GPIO as GPIO

# Set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up the variables for the LED, Buzzer, and switch pins
LEDRed = 18
LEDYellow = 23
LEDGreen = 24
PINBuzzer = 22
SWITCHPin = 25

# Set up each of the input (switch) and output (LEDs, Buzzer) pins
GPIO.setup(SWITCHPin,GPIO.IN)
GPIO.setup(LEDRed,GPIO.OUT)
GPIO.setup(LEDYellow,GPIO.OUT)
GPIO.setup(LEDGreen,GPIO.OUT)
GPIO.setup(PINBuzzer,GPIO.OUT)

# Define a function for the intial stae (Green LED on, rest off)
# Pedestrian LEDs, Red(on), Green(off)
def StartGreen():
    GPIO.output(LEDGreen,GPIO.HIGH)
    GPIO.output(LEDRed,GPIO.LOW)
    GPIO.output(LEDYellow,GPIO.LOW)
# Turn the Green off and the amber on for 3 seconds
# Pedestrian Red stays lit
def SteadyAmber():
    GPIO.output(LEDGreen,GPIO.LOW)
    GPIO.output(LEDRed,GPIO.LOW)
    GPIO.output(LEDYellow,GPIO.HIGH)
    time.sleep(3)

# Turn the Amber off, and then red on for 1 second
def SteadyRed():
    GPIO.output(LEDGreen,GPIO.LOW)
    GPIO.output(LEDRed,GPIO.HIGH)
    GPIO.output(LEDYellow,GPIO.LOW)
    time.sleep(1)

# Sound the buzzer for 4 seconds, Pedsestrian LEDs
# Green (on), Red (off)
def StartWalking():
    GPIO.output(PINBuzzer,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(PINBuzzer,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(PINBuzzer,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(PINBuzzer,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(PINBuzzer,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(PINBuzzer,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(PINBuzzer,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(PINBuzzer,GPIO.LOW)
    time.sleep(0.5)

# Turn the buzzer off and wait for 2 seconds
# Pedestrian Green to flash
def DontWalk():
    GPIO.output(PINBuzzer,GPIO.LOW)
    time.sleep(2)

# Flash the Amber for 6 seconds
# Flash the Pedestrian Green for 6 seconds
def FlashingAmberGreen():
    GPIO.output(LEDYellow,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.LOW)
    time.sleep(0.5)

# Flash the Amber for 1 more second
# Turn the Pedestrian Red (on) and Green (off)
def FlashingAmber():
    GPIO.output(LEDYellow,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LEDYellow,GPIO.LOW)
    time.sleep(0.5)

# Go through the traffic light sequence by calling each function
# one after the other
def TrafficLightSequence():
    SteadyAmber()
    SteadyRed()
    StartWalking()
    DontWalk()
    FlashingAmberGreen()
    FlashingAmber()
    StartGreen()

os.system('clear') # Clears the screen
print ("Traffic Lights")
# Initialise the traffic lights
StartGreen()

# Here is the loop that waits at least 20 seconds before
# stopping the cars if the button has been pressed

while True: # Loop around forever
    ButtonNotPressed = True # Button has not been pressed
    start = time.clock() #records the current time
    while ButtonNotPressed: # While the button has not been pressed
        time.sleep(0.1) # Wait for 0.1 seconds
        if GPIO.input(SWITCHPin) == False:  # If the button is pressed    
            ButtonNotPressed = False # Button has been pressed
            if time.clock()-start<=20:
                time.sleep (20-start)
        TrafficLightSequence() # Run the traffic light sequence
GPIO.cleanup()
 
