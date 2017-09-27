import RPi.GPIO as GPIO
import time

led=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
pwm=GPIO.PWM(led,500)
pwm.start(100)

while 1:
    i=1;
    for i in range(1,101):
        
        fvalue=int(i)
        pwm.ChangeDutyCycle(fvalue)
        time.sleep(.2)
    
