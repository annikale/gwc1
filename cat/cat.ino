/* This is a comment. We're coding cat whiskers
 * This comment can be multiple lines.
 * Otherwise, we'll just call // for single line comments
 */

  // We have two whiskers, data type: int
  int leftWhisker = 5 ;
  int rightWhisker = 7 ;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  // Declares that my whiskers are inputs
  pinMode(leftWhisker, INPUT);
  pinMode(rightWhisker, INPUT);
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

  if (lwValue == 0 && rwValue == 00) {
    Serial.println("Left and Right pressed!");
  } else if (lwValue == 0) {
    Serial.println("Left pressed!");
  } else if (rwValue == 0) {
    Serial.println("Right pressed!");
  } else {
    Serial.println("Neither pressed!");
  }
  
  // Left: ####
  // Right: ###

  // 100 milliseconds delay as to not overwhelm Serial Port
  delay(500); 
}
