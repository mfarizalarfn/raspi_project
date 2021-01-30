#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
from gpiozero import Buzzer
#from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
reader = SimpleMFRC522()
GPIO.setup(17,GPIO.OUT)

#GPIO.setmode(GPIO.BOARD)
buzzer = Buzzer(17)

try:
        text = raw_input("Please enter Data Name : ")
        print("Now place your tag to write")
        reader.write(text)
        print("Data recorded")
	GPIO.setup(18,GPIO.OUT)
	GPIO.output(18,GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(18,GPIO.LOW)
	time.sleep(0.2)
	GPIO.output(18,GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(18,GPIO.LOW)
	time.sleep(0.2)
	
	GPIO.output(17,GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(17,GPIO.LOW)
	time.sleep(0.5)
	#buzzer.on()
	#sleep(0.5)
	#buzzer.off()
	#sleep(0.5)

finally:
        #GPIO.cleanup()
	buzzer.close()
