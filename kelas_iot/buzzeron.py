from gpiozero import Buzzer

buzzer = Buzzer(17)

while True:
	buzzer.beep()
	buzzer.on()
