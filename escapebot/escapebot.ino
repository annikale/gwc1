/* This is a comment. We're coding cat whiskers
 * This comment can be multiple lines.
 * Otherwise, we'll just call // for single line comments
 */

#include <Servo.h>

const int photoResistor = A0;
const int threshold = 511; 

int sensorReading = 0;

  // We have two whiskers, data type: int
const int leftWhisker = 5 ;
const int rightWhisker = 7 ;

  int blueLED = A0;

  Servo servoLeft;
  Servo servoRight;
  
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  // Declares that my whiskers are inputs
  pinMode(leftWhisker, INPUT);
  pinMode(rightWhisker, INPUT);

  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(1459);  //left 1495 right 1452 = still servos = left 1496 right 1469 
  servoRight.writeMicroseconds(1535); // left 1469 right 1496 = move forward 
  //left 1510 right 1418 = move backward
  //left 1400 right 1390 = turn 180 for 2500 ms
}

//custom functions

void moveRobo() {
  servoLeft.writeMicroseconds(1459);
  servoRight.writeMicroseconds(1535);
}

void stopRobo() {
  servoLeft.writeMicroseconds(1495);  
  servoRight.writeMicroseconds(1452);
  delay(100);
}
void reverseRobo() {
  servoLeft.writeMicroseconds(1520);  
  servoRight.writeMicroseconds(1408);
  delay(3500);
}
void turnRobo() {
  servoLeft.writeMicroseconds(1400);  
  servoRight.writeMicroseconds(1390);
  delay(1800);
}
void rightturnRobo(){
  servoLeft.writeMicroseconds(1500);  
  servoRight.writeMicroseconds(1570);
  delay(1500);
}
void leftturnRobo(){
  servoLeft.writeMicroseconds(1400);  
  servoRight.writeMicroseconds(1390);
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:

  // This allows my arduino to see the data I want
  int lwValue = digitalRead(leftWhisker);
  int rwValue = digitalRead(rightWhisker);

  // How do I see the information from above?
  Serial.print("Left: ");
  Serial.println(lwValue);
  Serial.print("Right: ");
  Serial.println(rwValue);
  Serial.println(" "); // Prints an additional space for tidiness

  moveRobo();

  if (lwValue == 0 && rwValue == 00) {
    Serial.println("Left and Right pressed!");
    stopRobo();
    reverseRobo();
    turnRobo();
    loop();
  } else if (lwValue == 0) {
    Serial.println("Left pressed!");
    stopRobo();
    reverseRobo();
    rightturnRobo();
    loop();
  } else if (rwValue == 0) {
    Serial.println("Right pressed!");
    stopRobo();
    reverseRobo();
    leftturnRobo();
    loop();
  } else {
    Serial.println("Neither pressed!");
  }
  
  // Left: ####
  // Right: ###

  // 100 milliseconds delay as to not overwhelm Serial Port
  delay(500); 

    // put your main code here, to run repeatedly:
  sensorReading = analogRead(photoResistor);
  Serial.println(sensorReading);

  if (sensorReading <= 511){
    Serial.println("Ah! It's dark!");
    digitalWrite(blueLED, HIGH);
    delay(500);
    digitalWrite(blueLED, LOW);
    delay(500);
    digitalWrite(blueLED, HIGH);
    delay(500);
    digitalWrite(blueLED, LOW);
    delay(500);
    
  }
  delay(100);
}



