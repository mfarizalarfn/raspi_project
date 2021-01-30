import RPi.GPIO as GPIO
import time
from gpiozero import Buzzer

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

buzzer = Buzzer(17)

while True:
	print "LED on"
	GPIO.output(18,GPIO.HIGH)
	time.sleep(0.3)
	print "LED off"
	GPIO.output(18,GPIO.LOW)
	time.sleep(0.3)
	#buzzer.beep()
	buzzer.on()
	time.sleep(0.5)
	buzzer.off()
	time.sleep(0.5)
	#GPIO.output(27,GPIO.HIGH)
