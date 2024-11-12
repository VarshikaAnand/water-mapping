#include <TinyGPS++.h>
#include <SoftwareSerial.h>

#define trigPin 9
#define echoPin 10
#define rxPin 4   // GPS RX pin
#define txPin 3   // GPS TX pin

TinyGPSPlus gps;
SoftwareSerial gpsSerial(rxPin, txPin);  // Initialize software serial for GPS

bool isMeasuring = false;

void setup() {
  Serial.begin(9600);           // Start serial communication for PC
  gpsSerial.begin(9600);        // Start serial communication for GPS
  pinMode(trigPin, OUTPUT);     // Set the trigPin as an output
  pinMode(echoPin, INPUT);      // Set the echoPin as an input
}

void loop() {
  // Read GPS data
  while (gpsSerial.available() > 0) {
    gps.encode(gpsSerial.read());
  }

  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');

    if (command == "start") {
      isMeasuring = true;
      Serial.println("Measurement started");
    } 
    else if (command == "fire" && isMeasuring) {
      long distance = measureDistance();
      String gpsData = getGpsCoordinates();
      Serial.print("Depth: ");
      Serial.print(distance);
      Serial.print("; Coordinates: ");
      Serial.println(gpsData);
    } 
    else if (command == "end") {
      isMeasuring = false;
      Serial.println("Measurement ended");
    }
  }
}

long measureDistance() {
  long duration, distance;
  
  // Clear the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Send a 10µs pulse to trigPin
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the echoPin and calculate the duration
  duration = pulseIn(echoPin, HIGH);

  // Convert duration to distance in cm (adjust for water speed of sound)
  distance = duration * 0.1481/ 2;

  return distance;
}

String getGpsCoordinates() {
  if (gps.location.isUpdated()) {
    String latitude = String(gps.location.lat(), 6);
    String longitude = String(gps.location.lng(), 6);
    return latitude + "," + longitude;
  } else {
    return "NoFix";
  }
}
