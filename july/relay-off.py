import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)
GPIO.output(26,GPIO.LOW)
GPIO.setwarnings(False)
GPIO.output(26,True)
GPIO.cleanup()
