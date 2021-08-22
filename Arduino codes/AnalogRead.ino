int Pin = A0;
int Pin1 = A1;
int readVal;
int readVal1;
float V;
float V1;
void setup() {
  // put your setup code here, to run once:
  pinMode(Pin,INPUT);
  //pinMode(Pin1, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  readVal = analogRead(Pin);
  V = (5./1023.)*readVal;
  //Serial.print("Sensor 1: ");
  Serial.println(V);
  //Serial.print(", ");

  readVal1 = analogRead(Pin1);
  V1 = (5./1023.)*readVal1;
  //Serial.print("Sensor 2: ");
  Serial.println(V1);
  //Serial.print(", ");
  delay(1000);
}
