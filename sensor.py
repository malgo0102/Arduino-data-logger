#serial monitor must be closed - application listens on one port

import serial
#from serial import Serial
import time
import pandas as pd         #for parsing .csv file
import matplotlib.pyplot as plt    #for making plots
from apscheduler.schedulers.blocking import BlockingScheduler         #Advanced Python scheduler

       

arduino = serial.Serial('COM10', 9600)          # create Serial port object called arduino with correct port and baudrate
time.sleep(3)           # wait 3 sec for communication to establish

def writeToFile():

    arduino.write("1".encode('utf-8'))          # encode the b'\n'

    msg = arduino.readline()
    decodedLine = msg.decode('utf-8')
    print (decodedLine)         # decode the b'\n'

    file = open("sensorData.csv", "a+")         #open a file for writing and create if it doesn't exist
    file.write(decodedLine)         #write data to the file
    file.close()            #close the file when done

print("*******************************\nHumidity and temperature sensor\n*******************************\n")

scheduler = BlockingScheduler()
scheduler.add_job(writeToFile, 'interval', seconds = 5)
scheduler.start()

