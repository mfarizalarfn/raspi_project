import RPi.GPIO as GPIO
import time

in1 = 16
in2 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.output(in1, True)
GPIO.output(in2, True)

try:
	while True:
		GPIO.setwarnings(False)
		print("Pilihan : \n 1. Hidupkan Doorlock \n 2. Matikan Doorlock \n 3. Hidupkan Pompa Air \n 4. Matikan Pompa Air")
		pilih = int(input("Pilih Menu (1/2/3/4) : "))
		if pilih == 1:
			GPIO.setup(in1, GPIO.OUT)
			GPIO.output(in1, False)
		elif pilih == 2:
			GPIO.setup(in1, GPIO.OUT)
			GPIO.output(in1, GPIO.LOW)
			GPIO.setwarnings(False)
			GPIO.output(in1, True)
			#GPIO.cleanup()
		elif pilih == 3:
			GPIO.setup(in2, GPIO.OUT)
			GPIO.output(in2, False)
		elif pilih == 4:
			GPIO.setup(in2, GPIO.OUT)
			GPIO.output(in2, GPIO.LOW)
			GPIO.setwarnings(False)
			GPIO.output(in2, True)
			#GPIO.cleanup()
		else:
			print("!!! === PILIHAN ANDA TIDAK ADA === !!!")



except KeyboardInterrupt:
	GPIO.cleanup()
	
