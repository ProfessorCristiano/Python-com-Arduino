String line         = "";
bool stringComplete = false;
int Tom=11;
#define C4  262
#define D4  294
#define E4  330
#define F4  349
#define G4  392
#define A4  440
#define B4  494

void setup() {
  Serial.begin(9600);
  pinMode(Tom,OUTPUT);
  tone(Tom, A4, 200);
  delay(300);
  tone(Tom, A4, 200);
  delay(300);
}
 
void loop() {
  serialEvent();
  if (stringComplete){
    if (line.equals("A\n")){
       tone(Tom, A4, 1000);
       delay(1000);

    }
    else if (line.equals("B\n")){
      tone(Tom, B4, 1000);
       delay(1000);
    }
    else if (line.equals("C\n")){
      tone(Tom, C4, 1000);
       delay(1000);
    }
    else if (line.equals("D\n")){
      tone(Tom, D4, 1000);
       delay(1000);
    }
    else if (line.equals("E\n")){
      tone(Tom, E4, 1000);
       delay(1000);
    }
    else if (line.equals("F\n")){
      tone(Tom, F4, 1000);
       delay(1000);
    }
    else if (line.equals("G\n")){
      tone(Tom, G4, 1000);
       delay(1000);
    }
    
    stringComplete = false;
    line = "";
  }
 
}
 
void serialEvent(){
  while(Serial.available()){
    char inChar = (char)Serial.read();
    line += inChar;
    if (inChar == '\n'){
      stringComplete = true;
      Serial.print(line);
    }
  }
}
