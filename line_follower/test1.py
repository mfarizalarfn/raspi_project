import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(2,IO.IN) #GPIO 2 -> Kiri IR out
IO.setup(3,IO.IN) #GPIO 3 -> Kanan IR out

IO.setup(20,IO.OUT) #GPIO 4 -> Motor 1 terminal A
IO.setup(21,IO.OUT) #GPIO 14 -> Motor 1 terminal B

while 1:

    if(IO.input(2)==True and IO.input(3)==True): #both while move forward     
        IO.output(20,True) #1A+
        IO.output(21,True) #1B-

    elif(IO.input(2)==False and IO.input(3)==True): #turn right  
        IO.output(20,True) #1A+
        IO.output(21,False) #1B-

    elif(IO.input(2)==True and IO.input(3)==False): #turn left
        IO.output(20,False) #1A+
        IO.output(21,True) #1B-

    else:  #stay still
        IO.output(20,False) #1A+
        IO.output(21,False) #1B-
