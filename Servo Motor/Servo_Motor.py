import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)

pwm=GPIO.PWM(17,50)

pwm.start(0)

def setAngle(angle):

    duty= angle/18 +2
    GPIO.output(17,True)
    pwm.ChangeDutyCycle(duty)
    sleep(0.5)
    GPIO.output(17,False)
    pwm.ChangeDutyCycle(0)

setAngle(90)


def vasEtViens(nbDeFois,angle):
    for i in range(nbDeFois):
        setAngle(angle)
        sleep(0.5)
        setAngle(0)



#vasEtViens(5,180)


pwm.stop()
GPIO.cleanup()











