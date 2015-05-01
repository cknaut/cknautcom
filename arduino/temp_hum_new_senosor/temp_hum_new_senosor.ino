// Example testing sketch for various DHT humidity/temperature sensors
// Written by ladyada, public domain

#include "DHT.h"

#define DHTPIN 4    // what pin we're connected to

// Uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 11 
//#define DHTTYPE DHT22   // DHT 22  (AM2302)
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

// Connect pin 1 (on the left) of the sensor to +5V
// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1
// to 3.3V instead of 5V!
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor for normal 16mhz Arduino
DHT dht(DHTPIN, DHTTYPE);
// NOTE: For working with a faster chip, like an Arduino Due or Teensy, you
// might need to increase the threshold for cycle counts considered a 1 or 0.
// You can do this by passing a 3rd parameter for this threshold.  It's a bit
// of fiddling to find the right value, but in general the faster the CPU the
// higher the value.  The default for a 16mhz AVR is a value of 6.  For an
// Arduino Due that runs at 84mhz a value of 30 works.
// Example to initialize DHT sensor for Arduino Due:
//DHT dht(DHTPIN, DHTTYPE, 30);



#include <SPI.h>
#include <Ethernet.h>
#include <stdio.h>
#include <Wire.h>
#include "Adafruit_MCP9808.h"
// Create the MCP9808 temperature sensor object
Adafruit_MCP9808 tempsensor = Adafruit_MCP9808();


// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192,168,1,177);

// Initialize the Ethernet server library
// with the IP address and port you want to use 
// (port 80 is default for HTTP):
char server[] = "www.cknaut.com";
EthernetClient client;



void setup() {
  Serial.begin(9600); 
  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip);
  dht.begin();
    // Make sure the sensor is found, you can also pass in a different i2c
  // address with tempsensor.begin(0x19) for example
  if (!tempsensor.begin()) {
    Serial.println("Couldn't find MCP9808!");
    while (1);
  }      
}

void loop() {
  tempsensor.shutdown_wake(1); // shutdown MSP9808 - power consumption ~0.1 mikro Ampere    
  // Wait a 60 seconds between measurements.
  delay(50000);
  
  tempsensor.shutdown_wake(0); // wake up MSP9808 - power consumption ~200 mikro Ampere

  // Reading humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius
  float t = tempsensor.readTempC();
  
  // Check if any reads failed and exit early (to try again).
  if (isnan(h)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
 
  // Check if any reads failed and exit early (to try again).
  if (isnan(t)) {
    Serial.println("Failed to read from Adafruit sensor!");
    return;
  }
 
 //conversion of temperatur to strings and creating of request
  char temp[3];
  char hum[3];
  String tempAsString;
  String humAsString;
  dtostrf(t,1,0,temp);
  dtostrf(h,1,0,hum);
  tempAsString = String(temp);
  humAsString = String(hum);
  Serial.println("Temp is: " + tempAsString);
  Serial.println("Hum is: " + humAsString);
  String request = "GET /temp/add_data/temp=" + tempAsString + "&hum=" + humAsString + "/ HTTP/1.1";

  Serial.println("connecting...");

  // if you get a connection, report back via serial:
  if (client.connect(server, 80)) {
    Serial.println("connected");
    // Make a HTTP request:
    client.println(request);
    client.println("Host: www.cknaut.com");
    client.println("User-Agent: Arduino");
    client.println("Connection: close");
    client.println();
    client.println();
  } 
  else {
    // kf you didn't get a connection to the server:
    Serial.println("connection failed");
  }
  client.stop(); 
 Serial.println("connection stopped"); 
}
