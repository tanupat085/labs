int ledPin= 13;
int inputPin= 3;
int value= digitalRead(inputPin);
void setup(){
  pinMode(ledPin, OUTPUT);
  pinMode(inputPin, INPUT);
}

void loop(){
  if (value == HIGH)
  {
    digitalWrite(ledPin, HIGH);
    delay(1000) ;
    Serial.print (value);
  }

  else
  {
    digitalWrite(ledPin, LOW);
    Serial.print(value);

delay(1000) ;
  }
}
