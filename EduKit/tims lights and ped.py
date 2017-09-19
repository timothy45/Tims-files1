
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
button = Button(25)


def ButtonCheck():# Check if button is pushed
    
 # If the button is pressed, button.is_pressed will be 'true'
    if (button.is_pressed):
        print("Button pressed")
        time.sleep(5) # Sleep for 1 second
        PedRed()
             
    else:     
        print("Dont walk")

time.sleep(0.5) # Sleep for 0.5 seconds


def ButtonLoop():# Added to keep checking if button is pushed
    y=5
    while y>=0:
        ButtonCheck()
        time.sleep(0.5)
        y=y-1

def StartGreen():
    red.off()
    green.on()
    ButtonLoop()
    

def SteadyAmber():
    green.off()
    yellow.on()
    ButtonLoop()
    

def SteadyRed():
    green.off()
    yellow.off()
    
    red.on()
    ButtonLoop()

def PedRed():#What happens when button pressed
    red.off()
    green.off()
    yellow.on()
    z=5 #Flashes amber
    while z>=0:
        yellow.on()
        time.sleep(0.5)
        yellow.off()
        time.sleep(0.5)
        print (z)
        z=z-1
    print ("walk")
    red.on()
    time.sleep(5)
    
def TrafficLightSequence():#Sequnce for normaL OPERATION
    StartGreen()
    SteadyAmber()
    SteadyRed()
    
def Alloff():
     green.off()
     red.off()
     yellow.off()

x=5 #loop for how long to run sequnce
while x>=0:
    TrafficLightSequence()
    x=x-1
    
Alloff()  

    
