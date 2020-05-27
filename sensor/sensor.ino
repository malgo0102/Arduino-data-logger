//Requires DHT sensor library https://github.com/adafruit/DHT-sensor-library
#include <DHT.h>                        //humidity and temperature censor library
#include <DHT_U.h>

#define dataPin 8                       //define pin no. connected to censor
#define dhtType DHT22                   //define type of sensor

DHT dht(dataPin, dhtType);              //create DHT object

void setup() {

  Serial.begin(9600);                   //open serial port, sets data rate to 9600 bps
  dht.begin();

}

  float data;                           //one read from a sensor
  float arr[100];                       //array filled with data collected between start and stop logging triggers
  int i = 0;                            //index helper used in populateArray() and printData()
  int trigger;                          //Python request handler
  bool isReading = false;               //whether the sensor is logging or not
  bool isTemperatureSensor;             //whether the sensor is measuring temperature or humidity
  

void * populateArray(float data, float *dataArr){     //populate the array with data
  dataArr[i++] = data;
  return dataArr;
}

void printData(float *dataArr) {        //send data over to Python program (serial monitor)
  int j;
  for (j = 0; j < i; j++){              //print the newest data from index 0 to i
    Serial.print(dataArr[j]);           //dereferencing pointer and extracting value
    Serial.print(",");
  }
  Serial.print("\n");
}
  
void loop() {
  delay(2000);

  int readData = dht.read(dataPin);     //read the data from the sensor
  
  if(Serial.available()){               //handle requests from Python program
    trigger = Serial.read();
  }

  
  if(trigger == '1'){                   // choose the temperature sensor
    isTemperatureSensor = true;              
  }
  if(trigger == '2'){                   // choose the humidity sensor
    isTemperatureSensor = false;       
  }
  if(trigger == '3'){                   //start logging
    isReading = true;
  }
  if(trigger == '4'){                   //stop logging
    isReading = false;
  }  
  if(trigger == '5'){
    printData(arr);                     //send data over to Python program (serial monitor)
    memset(arr, 0, sizeof(arr));        //clear the array after sending the data
  }
 

  if (isReading){                       //select sensor based on the trigger
    if (isTemperatureSensor){
      data = dht.readTemperature();  
    }
    if (!isTemperatureSensor){
      data = dht.readHumidity();  
    }
    if (isnan(data)){
      Serial.println(F("\n\nFailed to read from the sensor\n"));
    }      
    populateArray(data, arr);           //returns array that is passed in the printData(arr)
  }
}


 
