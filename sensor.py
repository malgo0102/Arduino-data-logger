#serial monitor must be closed - application listens on one port
import serial
import time
import pandas as pd                 #for parsing .csv file
import matplotlib.pyplot as plt     #for making plots
import os

       

arduino = serial.Serial('COM10', 9600)          # create Serial port object called arduino with correct port and baudrate
time.sleep(3)                                   # wait 3 sec for communication to establish


sensor1 = "Temperature sensor"
sensor2 = "Humidity sensor"
filename = ""

def start(sensor1, sensor2):
    while True:
        chooseSensor(sensor1, sensor2)
        printMenu()

def chooseSensor(snsr1, snsr2):
    global filename
    menuSensor = """
    Welcome!
    Choose the sensor: 
    1 %s
    2 %s
    """ % (snsr1,snsr2)
    print (menuSensor)

    userInput = input()
    if(userInput=="1"):                               # choose temperature sensor
        filename = "data_temperature.csv"
        sensor = snsr1
        arduino.write("1".encode('utf-8'))          # encode the b'\n'
    elif (userInput=="2"):                            # choose humidity sensor
        filename = "data_humidity.csv"
        sensor = snsr2
        arduino.write("2".encode('utf-8'))          # encode the b'\n'
    else:
        print("\nWrong user input\n")
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

    userInput = input()
    if(userInput=="1"):
        print ("Started logging...\nPress any key to stop logging")
        startLogging()
        os.system('pause')
        stopLogging()
        print ("Stopped logging...\nPress any key to transmit data and save it in a file")
        os.system('pause')
        transmitData()
        print ("Transmitted and saved data...")
        printMenu()    
    elif (userInput=="2"):
        print ("Showing the plot...")
        showPlot()
        printMenu()
    elif (userInput=="3"):
        return
    else:
        print("\nWrong user input\n")
        printMenu()
        
def startLogging():
    arduino.write("3".encode('utf-8'))          # encode the b'\n'

def stopLogging():
    arduino.write("4".encode('utf-8'))          # encode the b'\n'

def transmitData():
    arduino.write("5".encode('utf-8'))          # encode the b'\n'

    writeToFile()

def writeToFile():
    global filename
    msg = arduino.readline()
    decodedLine = msg.decode('utf-8')
    print (decodedLine)                 # decode the b'\n'

    file = open(filename, "a+")         #open a file for writing and create if it doesn't exist
    file.write(decodedLine)             #write data to the file
    file.close()                        #close the file when done


def showPlot():
    None



print("\t*******************************\n\tHumidity and temperature sensor\n\t*******************************\n")
start(sensor1,sensor2)