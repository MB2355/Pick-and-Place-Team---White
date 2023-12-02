#include <Servo.h>

Servo servo01;
Servo servo02;
Servo servo03;
Servo servo04;
Servo servo05;
Servo servo06;

void setup() {
  Serial.begin(9600); // Initialize serial communication
  // Attach servo pins
  servo01.attach(5);
  servo02.attach(6);
  servo03.attach(7);
  servo04.attach(8);
  servo05.attach(9);
  servo06.attach(10);
  int speed = 5;
  
}

void loop() {
    int angles[6]; // Array to store the angles
    // Move each servo to the corresponding angle
    angles[0];
    for (int i = 0; i < angles[0]+1; i+=speed) {
        servo01.write(angles[0]);
    }
    angles[1];
    for (int i = 0; i < angles[1]+1; i+=speed) {
        servo01.write(angles[1]);
    }
    angles[2];
    for (int i = 0; i < angles[2]+1; i+=speed) {
        servo01.write(angles[2]);
    }
    angles[3];
    for (int i = 0; i < angles[3]+1; i+=speed) {
        servo01.write(angles[3]);
    }
    angles[4];
    for (int i = 0; i < angles[4]+1; i+=speed) {
        servo01.write(angles[4]);
    }
    angles[5];
    for (int i = 0; i < angles[5]+1; i+=speed) {
        servo01.write(angles[5]);
    }
    
  }
}
