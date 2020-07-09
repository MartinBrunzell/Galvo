#include <digitalWriteFast.h>

#include <stdlib.h>

char serial;                      
void setup()
{   
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);

   
}

void loop()
{ 
  if(Serial.available() > 0)
  {
      serial = Serial.read();
      Serial.println( serial, HEX);
      if (serial=='2')
      {
        digitalWrite(2,1);
        delay(100);                                     
        digitalWrite(2,0);       
      }
      if (serial=='3')
      {
        digitalWrite(3,1);
        delay(100);                                     
        digitalWrite(3,0);         

      }
      if (serial=='4')
      {                                      
        digitalWrite(4,HIGH);
                                    
        digitalWrite(4,LOW);         
      }
   }
}
