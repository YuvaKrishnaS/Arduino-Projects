#include <Servo.h>

const int Y_pin = A5; // analog pin connected to Y output



Servo myservo;  



int val; 
int mo = 13;   



void setup() {
  pinMode(mo, OUTPUT);

  myservo.attach(11); 

} 



void loop() {
  digitalWrite(mo, HIGH );

  val = analogRead(Y_pin);            

  val = map(val, 0, 1023, 0, 180);     

  myservo.write(val);                  

  delay(15);                           

}
