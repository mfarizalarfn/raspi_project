import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(4,True)
GPIO.cleanup()
