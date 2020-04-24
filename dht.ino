
int n1 = 4 ;
int n2 = 5 ;
int enB = 6;
void setup()
{
  pinMode(enB, OUTPUT);
  pinMode(n1, OUTPUT);
  pinMode(n2, OUTPUT);
  analogWrite(enB, 200);
}

void loop()
{
    digitalWrite(n2, HIGH);
    digitalWrite(n1, LOW);
}
