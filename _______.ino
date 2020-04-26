const int trigPin = 8;
const int echoPin = 10;
#include <Servo.h> 
Servo myservo; 
long duration;
int distance;
int a ;
void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
  myservo.attach(9); 
  myservo.write(0);
  delay(1000);
}
void ul() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
 
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  Serial.print("Distance: ");
  Serial.println(distance);
}
void loop() {
 ul();
  delay(1000);
  if(distance < 30){
a = 0;
  }
  if(distance >= 30){
    a = 1;
  }

  if(a == 0 ){
    delay(10000);
    ul();
    Serial.print("Distance2: ");
  Serial.println(distance);
    if (distance >= 30){
       myservo.write(30); 
       delay(2000);
       myservo.write(60); 
       delay(2000);
       myservo.write( 0);   
       delay(2000);
    }
  
             }
             delay(1000); 
}
