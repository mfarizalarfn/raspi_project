from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)

while True:
	buzzer.beep()
	buzzer.on()
	sleep(0.5)
	buzzer.off()
	sleep(0.3)
