#include <Servo.h>
#include <stdlib.h>
#define pin A0

char serial_line[100] ="";
int serial_line_length=0;
Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
 
void setup()
{
  Serial.begin(9600);
  Serial.setTimeout(1000);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode (pin, INPUT);
  myservo.attach(9);
}
 
void loop()
{
   int Time = 0;
   if (Serial.available() > 0)
  {
    serial_line_length = Serial.readBytesUntil(' ', serial_line, 100);
    Time = atoi(serial_line);
    Serial.println(Time);
//      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
//      delay(1000);                       // wait for a second
//      digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
//      delay(1000);
    if (Time)
    {
      for (pos = 60; pos <= 120; pos += 60) { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
        myservo.write(pos);              // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
      delay(Time * 30);
      for (pos = 120; pos >= 60; pos -= 60) { // goes from 180 degrees to 0 degrees
        myservo.write(pos);              // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
    }
  }
  int Open = 0;
  uint16_t value = analogRead (pin);
  uint16_t range = get_gp2d12 (value);
  Serial.println(range);
  uint16_t range0 = 0;
  if (range0 < 300 && range < 300)
  {
    range0 = range;
    //Open = 1;
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(100);                       // wait for a second
   }
  else if (range0 > 300 && range > 300)
   {
    range0 = range;
    //Open = 0;
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(100);
   }
   else{
    range0 = range;
   }
//  Open is the final result

 
}

uint16_t get_gp2d12 (uint16_t value) {
  if (value < 10) value = 10;
  return ((67870.0 / (value - 3.0)) - 40.0);
}
