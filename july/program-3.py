import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)

in1 = 16
in2 = 18
in3 = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)

GPIO.output(in1, True)
GPIO.output(in2, True)
GPIO.output(in3, True)

reader = SimpleMFRC522()

stop = False
try:
	#while True:
	print "Please tap your card"
	id, text = reader.read()

	if (id) == 102379184869:
		while True:
			print("Pilihan : \n 1. Hidupkan Doorlock \n 2. Matikan Doorlock \n 3. Hidupkan Pompa Air \n 4. Matikan Pompa Air \n 5. Hidupkan Lampu \n 6. Matikan Lampu \n 7. Exit")
			pilih = int(input("Pilih Menu (1/2/3/4/5/6/7) : "))
			if pilih == 1:
				GPIO.setup(in1, GPIO.OUT)
				GPIO.output(in1, False)
			elif pilih == 2:
				GPIO.setup(in1, GPIO.OUT)
				GPIO.output(in1, GPIO.LOW)
				GPIO.setwarnings(False)
				GPIO.output(in1, True)
			elif pilih == 3:
				GPIO.setup(in2, GPIO.OUT)
				GPIO.output(in2, False)
			elif pilih == 4:
				GPIO.setup(in2, GPIO.OUT)
				GPIO.output(in2, GPIO.LOW)
				GPIO.setwarnings(False)
				GPIO.output(in2, True)
			elif pilih == 5:
				GPIO.setup(in3, GPIO.OUT)
				GPIO.output(in3, False)
			elif pilih == 6:
				GPIO.setup(in3, GPIO.OUT)
				GPIO.output(in3, GPIO.LOW)
				GPIO.setwarnings(False)
				GPIO.output(in3, True)
				#GPIO.cleanup()	
			elif pilih == 7:
				print "Anda Telah Keluar dari Program"
				GPIO.cleanup()
				break	
			else:
				print("!!! === PILIHAN ANDA TIDAK ADA === !!!")
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
	else:
		print "DATA KOSONG"


finally:
	#print "Please tap your card again"
	#id,text = reader.read()
	GPIO.cleanup()


#except KeyboardInterrupt:
#	GPIO.cleanup()

GPIO.cleanup()
