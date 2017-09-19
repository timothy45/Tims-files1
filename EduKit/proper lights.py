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


def StartGreen():
    print('green')
    red.off()
    green.on()
    time.sleep(3)

def SteadyAmber():
    print('amber')
    green.off()
    yellow.on()
    time.sleep(3)

def SteadyRed():
    print('red')
    yellow.off()
    red.on()
    time.sleep(3)
 
def StartWalking():
    print('START WALKING')
    red.on()
    green.off
    yellow.off
    time.sleep(5)
 
def DontWalk():
    print('tim')
 
def FlashingAmberGreen():
    print('tim')
 
def FlashingAmber():
    print('tim')




def buttonPushed():
    while True: # Loop around forever
        ButtonNotPressed = True # Button has not been pressed
        start = time.time() # Records the current time
        while ButtonNotPressed: # While the button has not been pressed
            time.sleep(0.1) # Wait for 0.1s
            
            if (button.is_pressed): # If the button is pressed
                now = time.time()
                ButtonNotPressed = False # Button has been pressed
                print('button pressed')
                #StartWalking()
            
                if (now - start) <= 20: # If under 20 seconds
                    time.sleep (20 - (now - start)) # Wait until 20s is up
                    print('timer finished')
            
        print("so")
 
def TrafficLightSequence():
    StartGreen()
    buttonPushed()
    SteadyAmber()
    buttonPushed()
    SteadyRed()
 
os.system('clear') # Clears the terminal window
print("Traffic Lights")
x=5
while x<=5:
    TrafficLightSequence()
    x=x-1
d
