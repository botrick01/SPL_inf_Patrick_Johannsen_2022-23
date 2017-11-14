import RPi.GPIO as GPIO
import time
def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(2,GPIO.OUT)
def loop():
        GPIO.output(2,True)
        time.sleep(1)
        GPIO.output(2,False)
        time.sleep(0.5)
        GPIO.output(2,True)
        time.sleep(1)
setup()
while True:
        loop()