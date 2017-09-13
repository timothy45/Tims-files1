# CamJam Edukit 1 - Basics
# Worksheet 2 - LEDs
# Import Libraries
import time # A collection of time related commands
from gpiozero import LED # The LED functions from GPIO Zero
# Set pins 18, 23 and 24 to be LEDs
red = LED(18)
yellow = LED(23)
green = LED(24)

x=5
while x >=1:
    print (x)
    print("Red")
    red.on()

    
    time.sleep(5)
    yellow.on()
    print("Red and amber")

   
    time.sleep(3)

    yellow.off()
    red.off()

    print("Green")
    green.on()
    time.sleep(3)
    green.off()

    green.off()
    print("amber")    
    yellow.on()
    time.sleep(3)
    yellow.off()
    x=x-1
print("finished")
