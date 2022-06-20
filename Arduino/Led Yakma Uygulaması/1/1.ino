

void setup() {
  pinMode(7,OUTPUT);    // 7.pini çıkış pini olarak tanımladık
  pinMode(13,OUTPUT);
}

void loop() {
  digitalWrite(7,HIGH);		// 7.Pine elektrik gönder 
  digitalWrite(13,LOW);    // 7.Pine elektrik gönder 
  delay(10000);				// 10 saniye bekle 
  
  digitalWrite(13,HIGH);
  digitalWrite(7,LOW);		// 7.Pinden elektriği kes
  delay(10000);
}
