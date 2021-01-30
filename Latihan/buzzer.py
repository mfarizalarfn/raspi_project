#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(17, 100)
p.start(0)
try:
    while 1:
       	for dc in range(0, 50, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(1)
        for dc in range(100, -1, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(1)

except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
