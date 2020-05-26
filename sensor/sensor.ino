//Requires DHT sensor library https://github.com/adafruit/DHT-sensor-library

#include <DHT.h>    //humidity and temperature censor library
#include <DHT_U.h>

#define dataPin 8     //define pin no. connected to censor
#define dhtType DHT22     //define type of sensor

DHT dht(dataPin, dhtType);      //create DHT object

void setup() {

  Serial.begin(9600);     //open serial port, sets data rate to 9600 bps
  dht.begin();
}

  float tArr[100];
  float hArr[100];
  int i = 0;
  int trigger;
  bool isReading = false;


void * populateArray(float data, float *dataArr){     //populate the array with data
    dataArr[i++] = data;
    return dataArr;
}

void printData(float *dataArr) {     ////send data over to Python program (serial monitor)
  int j;
  for (j = 0; j < i; j++){       //print the newest data from index 0 to i
    Serial.print(dataArr[j]);    //dereferencing pointer and extracting value
    Serial.print(",");
  }
  Serial.print("\n");
}
  
void loop() {
  delay(2000);
  int readData = dht.read(dataPin);     //read the data from the sensor
  
  if(Serial.available()){      //handle requests from Python program
   trigger = Serial.read();
  }
  
  
  if(trigger == '1'){       //start logging
    isReading = true;
  }
  if(trigger == '2'){       //stop logging
    isReading = false;
  }  
  if(trigger == '3'){
    printData(/*"\nTemperature: ", */tArr);      //send data over to Python program (serial monitor)
    memset(tArr, 0, sizeof(tArr));        //clear the array after sending the data
  }

  if (isReading){
    float t = dht.readTemperature();      //read the temperature
    if (isnan(t)){
        Serial.println(F("\n\nFailed to read from the sensor\n"));
    }
    populateArray(t, tArr);      //populate the array with data
  }
}


 
