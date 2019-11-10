import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN)
GPIO.setup(18, GPIO.OUT)


try:
    time.sleep(4)
    
    while True:
        if GPIO.input(23):
            GPIO.output(18,True)
            time.sleep(0.5)
            GPIO.output(18,False)
            print("Mouvement détecté")
            time.sleep(5)
        time.sleep(0.1)
            
except:
    GPIO.cleanup()