import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,True)

time.sleep(100)

GPIO.output(18,False)

GPIO.cleanup()
