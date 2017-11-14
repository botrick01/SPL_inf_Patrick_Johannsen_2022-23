import RPi.GPIO as GPIO
import time
def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(2,GPIO.OUT)
def loop():
    eingabe = input()
    if(eingabe == "e"):
        GPIO.output(2,True)
    elif(eingabe == "a"):
        GPIO.output(2,False)
setup()
while True:
        loop()