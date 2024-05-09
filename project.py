import cv2
import numpy as np
import math
import time
import motors
import RPi.GPIO as GPIO
from PIL import Image
import picamera


from datetime import datetime

img_file = 'image.jpg'

img_file1 = 'im.jpg'

camera = picamera.PiCamera() 
camera.resolution = (1028, 720)
red = 0

def main():
    lcd_init()

    lcd_string("Self-Driving Car ",LCD_LINE_1)
    lcd_string(" Raspberry Pi ",LCD_LINE_2)

    time.sleep(3)

    while True:
        # Read Image

        lcd_byte(0x01,LCD_CMD) # 000001 Clear display
        lcd_string("Monitoring... ",LCD_LINE_1)

        camera.capture('image.jpg')
        
        img = cv2.imread('image.jpg')
        
        image = cv2.resize(img,(r_width,r_height))
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
        stop_cascade = cv2.CascadeClassifier('stop_sign.xml')
        stop = stop_cascade.detectMultiScale(gray, 1.3, 5)
        
        if len(stop) > 0 and flag == 0:
            lcd_string("SIGN : STOP",LCD_LINE_2)
            motors.stop()
            flag = 1
            time.sleep(2)
        else:
            flag = 0
        
        y=360
        x=0
        h=360
        w=1023
        image = img[y:y+h, x:x+w]
        
        lines = cv2.HoughLinesP(edged,1,np.pi/180,max_slider,minLineLength,maxLineGap)
        #print lines
        if lines is not None :
            #print(lines[0])
            for x in range(0, len(lines)):
                for x1,y1,x2,y2 in lines[x]:
                    cv2.line(image,(x1,y1),(x2,y2),(255,0,0),3)
                    theta=theta+math.atan2((y2-y1),(x2-x1))
                #print(theta)
            threshold=5
            #print theta
            motors.stop()
            if(theta>threshold):
                       motors.turnRight()
                       #lcd_string("SIGN:Right Turn",LCD_LINE_2)
                   #print("Go left")
            if(theta<-threshold):
                       motors.turnLeft()
                   #print("Go right")
            if(abs(theta)<threshold):
                if red == 0:         
                        motors.forward()
                   #print("Go straight")
            theta=0