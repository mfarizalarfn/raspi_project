import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
from gpiozero import Buzzer

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
#GPIO.setup(4,GPIO.OUT)
#GPIO.output(4,False)

buzzer = Buzzer(17)
reader = SimpleMFRC522()

#try:
stop = False
while True:
	try:
		print "Please tap your card"
		id, text = reader.read()

		if (id) == 102379184869:
			print "Lampu Menyala"
			print(text)
			buzzer.on()
			time.sleep(0.2)
			buzzer.off()
			time.sleep(0.2)
			buzzer.on()
			time.sleep(0.2)
			buzzer.off()
			time.sleep(0.2)
			while True:
			GPIO.setup(4,GPIO.OUT)
			GPIO.output(4,GPIO.HIGH)
		#break
	elif (id) == 184631823159:
		print "Lampu Mati"
		print(text)
		buzzer.on()
		time.sleep(0.3)
		buzzer.off()
		time.sleep(0.3)
		while True:
			GPIO.cleanup()
			#GPIO.setup(4,GPIO.OUT)
			#GPIO.output(4,GPIO.LOW)
		#break
	else:
		print "DATA KOSONG"

	continue
	#id,text = reader.read()
	print "Please tap your card again"
	id,text = reader.read()







#print(id)
#print(text)
#GPIO.output(4,GPIO.HIGH)
#GPIO.output(18,GPIO.HIGH)
#time.sleep(0.3)
#GPIO.output(18,GPIO.LOW)
#time.sleep(0.3)
#buzzer.on()
#time.sleep(0.5)
#buzzer.off()
#time.sleep(0.5)
#GPIO.setup(4,GPIO.OUT)
#GPIO.output(4,False)
#finally:
	#GPIO.cleanup()
