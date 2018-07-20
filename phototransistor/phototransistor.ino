const int photoResistor = A0;
const int threshold = 511; 

int sensorReading = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorReading = analogRead(photoResistor);
  Serial.println(sensorReading);

  if (sensorReading <= 511){
    Serial.println("Ah! It's dark!");
    delay(2000); 
  }
  delay(100);
}

