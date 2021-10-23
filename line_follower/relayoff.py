import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(21,GPIO.OUT)
GPIO.output(21,GPIO.LOW)
GPIO.setup(20,GPIO.OUT)
GPIO.output(20,GPIO.LOW)

GPIO.setwarnings(False)
GPIO.output(21,True)
GPIO.setup(20,True)
GPIO.cleanup()
