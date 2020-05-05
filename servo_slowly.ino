#include <Servo.h>
//red=5v //brown=gnd //orange=pinmode
Servo myservo;  

int pos = 0;    

void setup() {
  myservo.attach(9);  
}

void loop() {
  for (pos = 0; pos <= 180; pos += 1) { 
   
    myservo.write(pos);             
    delay(50);                       
  }
  for (pos = 180; pos >= 0; pos -= 1) { 
    myservo.write(pos);              
    delay(50);                       
  }
}
 
