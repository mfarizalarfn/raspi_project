import RPi.GPIO as GPIO
import time
from gpiozero import Buzzer

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

buzzer = Buzzer(17)

GPIO.output(18,GPIO.HIGH)
time.sleep(0.3)
GPIO.output(18,GPIO.LOW)
time.sleep(0.3)
buzzer.on()
time.sleep(0.5)
buzzer.off()
time.sleep(0.5)
