void setup(){
  Serial.begin(9600);
  pinMode(2,INPUT);
  pinMode(3,INPUT);
  pinMode(4,INPUT);
}
void loop(){
  
  if (digitalRead(2)==1){
    Serial.print(int(1));
    delay(1000);
  }
  if (digitalRead(3)==1){
    Serial.print(int(2));
    delay(100);
  }
  if (digitalRead(4)==1){
    Serial.print(int(3));
    delay(100);
  }
 
 
}

