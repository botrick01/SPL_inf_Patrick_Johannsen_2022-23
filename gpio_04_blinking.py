import RPi.GPIO as GPIO
import time
redlight = True
def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(2,GPIO.OUT)
        GPIO.setup(3,GPIO.OUT)
        GPIO.setup(4,GPIO.OUT)

        GPIO.output(2,True)
        GPIO.output(3,False)
        GPIO.output(4,False)
def loop():
    global redlight
    eingabe = input()
    if(eingabe == ""):
        if(redlight == True):
            redlight = False
            GPIO.output(3,True)
            time.sleep(2)
            GPIO.output(2,False)
            GPIO.output(3,False)
            GPIO.output(4,True)
        else:
            redlight = True
            i = 0
            while(i < 3):
                i += 1
                GPIO.output(4,False)
                time.sleep(0.5)
                GPIO.output(4,True)
                time.sleep(0.5)
            GPIO.output(4, False)
            GPIO.output(3, True)
            time.sleep(1)
            GPIO.output(3,False)
            GPIO.output(2, True)

setup()
while True:
        loop()