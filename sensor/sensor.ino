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

  float tList[20];
  int i = 0;
  int trigger;
  bool isWrapped = false;


void populateArray(float data, float *dataArr){     //populate the array with data
  if (i<20){        // populate the array
    dataArr[i++] = data;
  }
  else {        //overwrite the array (clear)
    isWrapped = true;
    i = 0;
    dataArr[i++] = data;
  }
}

void printData(char *s, float *dataArr) {     ////send data over to Python program (serial monitor)
  Serial.print(s);
  int j;
  if (isWrapped){
    for(j = i; j < 20; j++){        //print the newest data from index i to 19 
      Serial.print(dataArr[j]);
      Serial.print(",");  
    }
  }
  for (j = 0; j < i; j++){       //print the newest data from index 0 to i
    Serial.print(dataArr[j]);
    Serial.print(",");
  }
}
  
void loop() {
  
  delay(2000);
  int readData = dht.read(dataPin);     //read the data from the sensor

  float t = dht.readTemperature();      //read the temperature
  if (isnan(t)){
      Serial.println(F("\n\nFailed to read from the sensor\n"));
  }

  populateArray(t, tList);      //populate the array with data
  
  if(Serial.available()){      //handle requests from Python program
   trigger = Serial.read();
  }
  if(trigger == '1'){
    printData("\nTemperature: ", tList);      //send data over to Python program (serial monitor)
  }
}


 
