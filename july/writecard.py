import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
from gpiozero import Buzzer

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
reader = SimpleMFRC522()

try:
        text = raw_input("Please enter Data Name : ")
        print("Now place your tag to write")
        reader.write(text)
        print("Data recorded")

finally:
        print("Selesai")
