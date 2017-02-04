int cnt=0;
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
  
  /*Serial.print(digitalRead(2));
  delay(10);
  Serial.print("\n");
  Serial.print(digitalRead(3));
  delay(10);
  Serial.print("\n");
  Serial.print(digitalRead(4));
  Serial.print("\n");
  delay(10);*/
  /*Serial.print(cnt);
  Serial.print("\n");
  cnt=cnt+1;*/
 
 
}

