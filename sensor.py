#serial monitor must be closed - application listens on one port

import serial
#from serial import Serial
import time
import pandas as pd         #for parsing .csv file
import matplotlib.pyplot as plt    #for making plots
import os

       

arduino = serial.Serial('COM10', 9600)          # create Serial port object called arduino with correct port and baudrate
time.sleep(3)           # wait 3 sec for communication to establish

def startLogging():
    arduino.write("1".encode('utf-8'))          # encode the b'\n'

def stopLogging():
    arduino.write("2".encode('utf-8'))          # encode the b'\n'

def transmitData():
    arduino.write("3".encode('utf-8'))          # encode the b'\n'

    writeToFile()

def showPlot():
    None

def writeToFile():
    
    msg = arduino.readline()
    decodedLine = msg.decode('utf-8')
    print (decodedLine)         # decode the b'\n'

    file = open("sensorData.csv", "a+")         #open a file for writing and create if it doesn't exist
    file.write(decodedLine)         #write data to the file
    file.close()            #close the file when done

sensor1 = "Temperature and humidity sensor"
sensor2 = "Radioactivity sensor"

def start(sensor1, sensor2):
    while True:
        chooseSensor(sensor1, sensor2)
        printMenu()

def chooseSensor(snsr1, snsr2):
    print("\t*******************************\n\tHumidity and temperature sensor\n\t*******************************\n")
    menuSensor = """
    Welcome!
    Choose the sensor: 
    1 %s
    2 %s
    """ % (snsr1,snsr2)
    print (menuSensor)

    userInput = int(input())
    if(userInput==1):
        sensor = snsr1
        arduino.write("1".encode('utf-8'))          # encode the b'\n'
    elif (userInput==2):
        sensor = snsr2
        arduino.write("2".encode('utf-8'))          # encode the b'\n'
    else:
        print("Wrong userInput\n")
        chooseSensor(snsr1, snsr2)
    
    print("You chose %s." % (sensor))

    
def printMenu():
    menu = """
    Press:
    1 to start the logging process
    2 open a plot with saved data
    3 change sensor
    """
    print (menu)

    userInput = int(input())
    if(userInput==1):
        print ("Starting logging...\nPress any key to stop logging")
        startLogging()
        os.system('pause')
        stopLogging()
        print ("Stopped logging...\nPress any key to transmit data and save it in a file")
        os.system('pause')
        transmitData()
        print ("Transmitted and saved data...")
        printMenu()
        
    elif (userInput==2):
        print ("Showing the plot...")
        showPlot()
        printMenu()
    elif (userInput==3):
        return
    else:
        print("Wrong userInput\n")
        printMenu()
        


start(sensor1,sensor2)