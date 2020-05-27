#serial monitor must be closed - application listens on one port
import serial
import time
import pandas as pd                 #for parsing .csv file
import os
       

arduino = serial.Serial('COM10', 9600)          # create Serial port object called arduino with correct port and baudrate
time.sleep(2)                                   # wait 2 sec for communication to establish

sensor1 = "Temperature sensor"
sensor2 = "Humidity sensor"
filename = ""

def start(sensor1, sensor2):
    """
    Start menu: choose sensor and later choose action.
    Takes two sensor names as the parameters.
    """
    while True:
        chooseSensor(sensor1, sensor2)
        printMenu()

def chooseSensor(snsr1, snsr2):
    """
    Sending trigger to arduino to choose sensor.
    Filename is assigned depending on sensor choice.
    """
    global filename
    menuSensor = """
    Welcome!
    Choose the sensor: 
    1 %s
    2 %s
    3 Exit
    """ % (snsr1,snsr2)
    print (menuSensor)

    userInput = input()
    if(userInput=="1"):                               # choose temperature sensor
        filename = "data_temperature.csv"
        sensor = snsr1
        arduino.write("1".encode('utf-8'))            # encode the b'\n'
    elif (userInput=="2"):                            # choose humidity sensor
        filename = "data_humidity.csv"
        sensor = snsr2
        arduino.write("2".encode('utf-8'))            # encode the b'\n'
    elif (userInput=="3"):   
        exit()                         
    else:
        print("\nWrong user input\n")
        return chooseSensor(snsr1, snsr2)
    
    print("You chose %s." % (sensor))

    
def printMenu():
    """
    Choose action(start and stop logging, transmit data) and send trigger to arduino.
    """

    menu = """
    Press:
    1 Start the logging process
    2 Change sensor
    3 Exit
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
        writeToFile()
        print ("Transmitted and saved data...")
    elif (userInput=="2"):
        return
    elif (userInput=="3"):   
        exit()    
    else:
        print("\nWrong user input\n")
        return printMenu()
        
def startLogging():
    """Send trigger to arduino to start logging."""
    arduino.write("3".encode('utf-8'))          # encode the b'\n'

def stopLogging():
    """Send trigger to arduino to stop logging."""
    arduino.write("4".encode('utf-8'))          # encode the b'\n'

def transmitData():
    """Send trigger to arduino to send back data."""
    arduino.write("5".encode('utf-8'))          # encode the b'\n'

def writeToFile():
    """
    Read data from arduino and save it in a chosen .csv file.
    File name depends on chosen sensor.
    """
    global filename
    msg = arduino.readline()
    decodedLine = msg.decode('utf-8')
    print (decodedLine)                 # decode the b'\n'

    file = open(filename, "a+")         #open a file for writing and create if it doesn't exist
    file.write(decodedLine)             #write data to the file
    file.close()                        #close the file when done


print("\t*******************************\n\tHumidity and temperature sensor\n\t*******************************\n")
start(sensor1,sensor2)