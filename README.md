# Water Bed Mapping
The aim of this project is to aid researchers, environmentalists and industries to gather information on local water bodies.​

The solution is a compact device that can be used to map out a water body's floor, in the form of a depth map. The distance is calculated from the surface of the water to the floor via ultrasonic signals. It provides easy operation for the user – just start the program and move the bobber across the water. The GPS module will take care of tracking the location for the final mapping.​
## Components used
- Arduino Uno
- SR04 Waterproof Ultrasonic Sensor
- Neo 6M GPS Module

## Ciruit
HC-SR04 Ultrasonic Sensor: VCC to 5v on Arduino, GND to GND, Trig pin to Digital Pin 9 and Echo Pin to Digital Pin 8.​

Neo 6M GPS Module: VCC to 3.3V, GND to GND, TX to RX Pin of Arduino and RX to TX Pin of Arduino. ​

## Future Scope
We can scale this project by using a more industrial grade sensor (such as SONAR) with higher accuracy and low distortions in readings.​

A proper floater or a boat-like structure can be used to conveniently record the depths in a more uniform manner.​

A WiFi or Bluetooth module can be integrated with the Arduino along with a portable power supply for remote operation. The whole device could be integrated into a remote-controlled water drone to map the body from the convenience of dry land.​

The mapping can also be integrated with a mobile app for remote access.​

## Example Mapping
![WhatsApp Image 2024-11-12 at 21 43 36_225ca011](https://github.com/user-attachments/assets/6ce7b352-64bb-4a0d-aefe-a4e7e7785cfa)
https://github.com/user-attachments/assets/35e7bf55-7758-4d24-bcf0-190563912913

