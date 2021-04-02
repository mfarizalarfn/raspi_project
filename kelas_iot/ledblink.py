import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)

while True:
	print "LED on"
	GPIO.output(2,GPIO.HIGH)
	time.sleep(0.5)
	print "LED off"
	GPIO.output(2,GPIO.LOW)
	time.sleep(0.5)
