# CamJam Edukit 1 - Basics
# Worksheet 7 - Traffic Lights Template

# Import Libraries
import os
import time
from gpiozero import LED, Button, Buzzer

# Set up variables for the LED, Buzzer and switch pins

# Define a function for the initial state (Green LED on, rest off)
# (If you have the second 'pedestrian' LEDs, turn the red on & green
# off)
def StartGreen():
    # Remember all code in the function is indented

# Turn the green off and the amber on for 3 seconds
# ('Pedestrian' red LED stays lit)
def SteadyAmber():
    # Remember all code in the function is indented

# Turn the amber off, and then the red on for 1 second
def SteadyRed():
    # Remember all code in the function is indented

# Sound the buzzer for 4 seconds
# (If you have the 'pedestrian' LEDs, turn the red off and green on)
def StartWalking():
    # Make the buzzer buzz on and off, half a second of
    # sound followed by half a second of silence

# Turn the buzzer off and wait for 2 seconds
# (If you have a second green 'pedestrian' LED, make it flash on and
# off for the two seconds)
def DontWalk():
    # Remember all code in the function is indented

# Flash the amber on and off for 6 seconds
# (And the green 'pedestrian' LED too)
def FlashingAmberGreen():
    # Remember all code in the function is indented

# Flash the amber for one more second
# (Turn the green 'pedestrian' LED off and the red on)
def FlashingAmber():
    # Remember all code in the function is indented

# Go throught the traffic light sequence by calling each function
# one after the other.
def TrafficLightSequence():
    # Remember all code in the function is indented

os.system('clear') # Clears the terminal
print("Traffic Lights")
# Initialise the traffic lights
StartGreen()

# Here is the loop that waits at least 20 seconds before
# stopping the cars if the button has been pressed
while True: # Loop around forever
    buttonNotPressed = True # Button has not been pressed
    start = time.time() # Records the current time (seconds since 1st January 1970)
    while buttonNotPressed: # While the button has not been pressed
        time.sleep(0.1) # Wait for 0.1s
        if (button.is_pressed): # If the button is pressed
            now = time.time()
            buttonNotPressed = False # Button has been pressed
            if (now - start) <= 20: # If under 20 seconds
                time.sleep (20 - (now - start)) # Wait until 20s is up
            TrafficLightSequence() # Run the traffic light sequence
