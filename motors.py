#######
# Author: James Poole
# Date: 23 April 2016
# jgaple@gmail.com
#
# motors.py
#######

import RPi.GPIO as GPIO
import time
from time import sleep
Motor1A = 05 
Motor1B = 06 

Motor2A = 13 
Motor2B = 19 


 
TRIG = 23 
ECHO = 24

#Set up all as outputs
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)


def forward():
        
        GPIO.output(TRIG, False)
        #print "Waitng For Sensor To Settle"
        time.sleep(0.07)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)                      
        GPIO.output(TRIG, False)                 

        while GPIO.input(ECHO)==0:               
            pulse_start = time.time()              

        while GPIO.input(ECHO)==1:               
            pulse_end = time.time()                

        pulse_duration = pulse_end - pulse_start 

        distance = pulse_duration * 17150        

        distance = round(distance, 2)            
     
        print "Distance:",distance,"cm"

        if  distance > 25:       
                print("Going Forwards")
                GPIO.output(Motor1A,GPIO.HIGH)
                GPIO.output(Motor1B,GPIO.LOW)
                GPIO.output(Motor2A,GPIO.HIGH)
                GPIO.output(Motor2B,GPIO.LOW)
        else:
                print("Stopping")
                GPIO.output(Motor1A,GPIO.LOW)
                GPIO.output(Motor1B,GPIO.LOW)
                GPIO.output(Motor2A,GPIO.LOW)
                GPIO.output(Motor2B,GPIO.LOW)

	

def backward():
	print("Going Backwards")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

	sleep(0.05)

def turnRight():
	print("Going Right")
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.HIGH)

	sleep(0.05)

def turnLeft():
	print("Going Left")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)

	sleep(0.05)

def stop():
	print("Stopping")
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.LOW)






