from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD

lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d7=11, cols=16, lines=2)

lcd.clear()

lcd.message('First print\n in LCD Display')
sleep(3)

for x in range(0,16):
	lcd.move_right()
	sleep(.1)
sleep(3)

for x in range(0, 16):
	lcd.move_left()
	sleep(.1)
