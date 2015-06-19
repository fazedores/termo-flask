// LM35.ino
byte temp = A0;

void setup()
{
	Serial.begin(9600);
	pinMode(temp, INPUT);
}

void loop()
{
	Serial.print((analogRead(temp) * 500.0) / 1023);
	Serial.println();
	delay(1000);
}
