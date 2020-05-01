#include <Servo.h> 
//red=5v //brown=gnd //orange=pinmode
Servo myservo;   
void setup() 

{ 
  myservo.attach(9); 
  myservo.write(0); 
  delay(2000);
         
} 
void loop() 
{          
       myservo.write(30); 
       delay(2000);
       myservo.write(50); 
       delay(2000);
       myservo.write( 0);   
       delay(2000);                 
}
 

 
 
 
 
