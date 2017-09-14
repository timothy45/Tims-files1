# CamJam Edukit 1 - Basics
# Worksheet 2 - LEDs
# Import Libraries
import time # A collection of time related commands
import os # Gives Python access to Linux commands
import RPi.GPIO as GPIO #Gives Python access to the GPIO pins
from gpiozero import LED # The LED functions from GPIO Zero
from gpiozero import Button # The GPIO Zero button functions

# Set pins 18, 23 and 24 to be LEDs
red = LED(18)
yellow = LED(23)
green = LED(24)
# Set pin 25 as a button input
buttonPin = Button(25)
GPIO.setup(ButtonPin, GPIO.IN)
GPIO.setmode(GPIO.BCM) #Set the GPIO pin naming mode
GPIO.setwarnings(False) #Supress warnings


def StartGreen():
    red.off()
    green.on()
    time.sleep(3)
    

def SteadyAmber():
    green.off()
    yellow.on()
    time.sleep(3)
    

def SteadyRed():
    yellow.off()
    red.on()
    time.sleep(3)
    

def TrafficLightSequence():
    
    StartGreen()
    SteadyAmber()
    SteadyRed()

def Alloff():
     green.off()
     red.off()
     yellow.off()
    

# CamJam Edukit 1 - Basics
# Worksheet 5 - Button

# Import Libraries
import os # Gives Python access to Linux commands
import time # Proves time related commands
from gpiozero import Button # The GPIO Zero button functions

# Set pin 25 as a button input
button = Button(25)

print("-------------")
print("Button + GPIO")
print("-------------")

# The commands indented after this ‘while’ will be repeated
# forever or until ‘Ctrl+c’ is pressed.
while True:
 # If the button is pressed, button.is_pressed will be 'true'
    if (button.is_pressed):
        print("Button pressed")
        time.sleep(1) # Sleep for 1 second
    else:
        os.system("clear") # Clears the screen
        print("Waiting for you to press the button")

    time.sleep(0.5) # Sleep for 0.5 seconds
