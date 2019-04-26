String line         = "";
bool stringComplete = false;
 
void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  digitalWrite(13,HIGH);
 
}
 
void loop() {
  serialEvent();
  if (stringComplete){
    if (line.equals("on\n")){
      digitalWrite(13,HIGH);
    }
    else if (line.equals("off\n")){
      digitalWrite(13,LOW);
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
