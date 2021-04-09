import RPi.GPIO as GPIO  # Import GPIO library
import time  # Import time library

GPIO.setmode(GPIO.BCM)  # Set GPIO pin numbering

TRIG = 23  # Associate pin 23 to TRIG
ECHO = 24  # Associate pin 24 to ECHO

GPIO.setup(TRIG, GPIO.OUT)  # Set pin as GPIO out
GPIO.setup(ECHO, GPIO.IN)  # Set pin as GPIO in

dist = False  # holds the distance from the hand...
# dist will be true if hand is less than 5cms or else false

flagTime = time.time()  # this takes in the inital time the program began
currentTime = time.time()  # this holds the passing time value

while (
    currentTime - flagTime <= 60):  # it will run only for 60sec and return false if it doesn't get the appropriate value
    GPIO.output(TRIG, False)  # this is to make sure that there is no signal
    time.sleep(2)  # initially to avoid errors

    GPIO.output(TRIG, True)  # Set TRIG as HIGH
    time.sleep(0.00001)  # Delay of 0.00001 seconds = 10 micro seconds
    GPIO.output(TRIG, False)  # Set TRIG as LOW

    while GPIO.input(ECHO) == 0:  # Check whether the ECHO is LOW
        pulse_start = time.time()  # Saves the last known time of LOW pulse

    while GPIO.input(ECHO) == 1:  # Check whether the ECHO is HIGH
        pulse_end = time.time()  # Saves the last known time of HIGH pulse

    pulse_duration = pulse_end - pulse_start  # Get pulse duration to a variable
    # pulse duration is in seconds and not micro seconds
    distance = pulse_duration * 17150  # Multiply pulse duration by 17150 to get distance
    # the velocity is 34300 cm/sec and the length is half of the the measured distance because
    # it is travelling in both the directions
    distance = round(distance, 2)  # Round to two decimal points

    if 2 <= distance <= 6:  # Check whether the distance is within range
        # this implementation of if condition is new...check it out
        dist = True
        break
    else:
        dist = False
    currentTime = time.time()
else:
    dist = False
