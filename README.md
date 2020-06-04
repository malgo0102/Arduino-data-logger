# Data logger with the Arduino Uno

- Collects data with a sensor
- Stores data in an array 
- Communicates with PC over serial port
- Saves data to a file

## I used:
- Python for UI 
- DHT22 sensor to read temperature and humidity data.

Data is saved with a timestamp to:
- root/data_temperature.csv 
- root/data_humidity.csv

Example of a single data reading: 2020-06-03 23:58:51.973248,23.10,23.20,

## Getting started:
1. Install Matplotlib:
    - https://matplotlib.org/users/installing.html

2. Install Pandas:
    - https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html

3. Upload sensor/sensor.ino to Arduino connected to DHT22

4. Download the DHT sensor library to Arduino libraries
    - https://github.com/adafruit/DHT-sensor-library

5. Run the program in the root directory: 
    - python sensor.py

//malg0102