import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(36, GPIO.IN) #PIR 1
GPIO.setup(33, GPIO.IN) #PIR 2

#GPIO.setup(16, GPIO.OUT) #BUzzer
GPIO.setup(32, GPIO.OUT) #LED D0
GPIO.setup(16, GPIO.OUT) #LED D1

try:
    time.sleep(2) # to stabilize sensor
    while True:
        i=GPIO.input(36)   #pir 1
        j=GPIO.input(33)   #pir 2
 
        if i==1:
            GPIO.output(32, True)  #first led
            time.sleep(0.5) #Buzzer turns on for 0.5 sec
            print("Object Detected at first PIR and led first glows!!!")
            GPIO.output(32, False)
            time.sleep(2) #to avoid multiple detection
        
        elif j==1:
            GPIO.output(16, True)  #second led
            time.sleep(0.5) #Buzzer turns on for 0.5 sec
            print("Object Detected at second PIR and led second glows!!!")
            GPIO.output(16, False)
            time.sleep(2) #to avoid multiple detection

        
        elif i==0 or j==0:
            print"No Detection",i
            time.sleep(2) #to avoid multiple detection

        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()
