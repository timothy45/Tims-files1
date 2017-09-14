# CamJam Edukit 1 - Basics
# Worksheet 5 - Button

# Import Libraries
import os # Gives Python access to Linux commands
import time # Proves time related commands
from gpiozero import Button # The GPIO Zero button functions
from gpiozero import LED # The LED functions from GPIO Zero

# Set pin 25 as a button input
button = Button(25)

# Set pins 18, 23 and 24 to be LEDs
red = LED(18)
yellow = LED(23)
green = LED(24)



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

def FlashRed():
    yellow.off()
    red.on()
    time.sleep(1)
    red.off()
    time.sleep(1)
    red.on()

def TrafficLightSequence():
    
    StartGreen()
    SteadyAmber()
    SteadyRed()
    StartGreen()
    
print("-------------")
print("Button + GPIO")
print("-------------")

# The commands indented after this ‘while’ will be repeated
# forever or until ‘Ctrl+c’ is pressed.
while True:
 # If the button is pressed, button.is_pressed will be 'true'
    if (button.is_pressed):
        print("Button pressed")
        green.off()
        FlashRed()
        
        time.sleep(5) # Sleep for 1 second
    else:
        os.system('clear') # Clears the screen
        print("Waiting for you to press the button")
        TrafficLightSequence()
    time.sleep(0.5) # Sleep for 0.5 seconds
    
