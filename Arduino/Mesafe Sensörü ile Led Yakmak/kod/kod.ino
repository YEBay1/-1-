#define echopin 8
#define trigpin 7 
#define led 2 

int mesafe=0;
int sure=0;
int buzzerPin=4;

void setup(){
pinMode(trigpin,OUTPUT);	// Mesafe sensörü üzerinde bulunan pinleri tanımlıyoruz  --> TrigPin ve EchoPin
pinMode(echopin,INPUT);
pinMode(led,OUTPUT);
Serial.begin(9600);
}

void loop(){
  digitalWrite(trigpin,HIGH);
  delayMicroseconds(1000);
  digitalWrite(trigpin,LOW);
  digitalWrite(echopin,HIGH);

  sure=pulseIn(echopin,HIGH);
  mesafe=(sure/2)/29.1;
  Serial.println(mesafe);

  delay(250);

  if (mesafe<5){   
  digitalWrite(led,HIGH);
}
 else {
  digitalWrite(led,LOW);}
}
  

}



/*
Setup() fonksiyonu, Arduino’ya yüklenmiş olan .ino uzantılı kod parçasının, Arduino başlatıldığında veya yeniden başlatıldığında ilk çalıştırılan kısmıdır. 
Setup() fonksiyonu, çalışma ortamını başlangıç için bizlere hazırlar ve görevini tamamladıktan sonra bir yeniden başlatmaya kadar tekrar çalıştırılmaz.

#include <Servo.h>
Servo servo;
    
int pinNo = 13;
 
void setup() {
  Serial.begin(9600);
  pinMode(pinNo,OUTPUT);
  servo.attach(9);
}
 
void loop() {
  
}

Yukarıdaki örnek  kod parçasında setup fonksiyonu kullanılarak Serial.begin() ile seri veri iletim hızının ayarlanması, pinMode() ile belirtilen pinin bir çıkış pini 
olarak kullanılacağının belirtilmesi ve servo.attach() tanımlanan servo nesnesinin hangi pini kullanacağının belirtilmesi yapılmıştır. Bu örnektende anlaşılacağı gibi 
setup() fonksiyonu ile ortam çalışmaya hazır hale getirilir.


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

loop() Fonksiyonu
Loop() fonksiyonu, setup fonksiyonu çalıştırıldıktan sonra çalıştırılır ve bir sonsuz döngü işlevi görür. 
Loop fonksiyonun bu sonsuz döngü özelliği kullanılarak sürekli tekrar edecek olan işlemlerimizin gerçekleştirilmesini sağlanır. 
Örneğin; Arduino’nun belkide en temel örneği olan Blink örneğinde olduğu gibi 1’er saniye aralıkla bir ledi yakmak ve söndürmek gibi tekrar eden bir işlemlerde 
kullanılabilir.

void setup() {
  Serial.begin(9600);
}
 
void loop() {
  int sensorValue = analogRead(A0);
  Serial.println(sensorValue);
  delay(1);        
}

Yukarıdaki örnek kod parçası olan Arduino’nun AnalogReadSerial örneğinde, Analog Ao pininden okunan değerin 1 ms aralıklarla seri monitör üzerinden ekrana yazılması 
işlemi yapılmaktadır ve bu işlem sürekli olarak tekrar edecektir.


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


PinMode Komutu ,arduino kartlarınızda bulunan sinyal pinlerini giriş veya 
çıkış olarak atayabilmenize olanak tanır.
Genellikle motor,led,buzzer gibi veri ilettiğimiz elemanlar çıkış birimi olarak 
tanımlanırken buton,sensör,gibi veri okuduğumuz elemanlar ise giriş olarak tanımlanmaktadır.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

HC-SR04 mesafe sensörü 2 cm ile 400 cm arasındaki mesafeleri ölçebilmektedir. Böyle bir aralık söz konusuyken ilk bakışta bunu dijital sinyallerle değil de analog 
sinyallerle yapması gerekiyor gibi duruyor ancak Hc-SR04 ultrasonik mesafe sensörü mesafeyi hesaplarken dijital sinyallerini kullanıyor. Ses sinyali üreten hc-sr04 
ultrasonik mesafe sensörüne ses sinyalinin sensörden çıkışı ve geri dönüşü arasında geçen süreyi hesaplayıp basit bir fizik formülünü (yol=hız X zaman) kullanarak 
aradaki mesafeyi hesaplatıyoruz. Yani analog sensörlerde olduğu gibi sensör bize direkt bir değer sunmuyor. Sensör üzerinde bulunan Trig pini sensörün yayılmasını 
tetikliyor Echo pini de yüzeye çarpıp geri dönen ses sinyalini sensöre geldiğinde yakalıyor.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pulseIn() fonksiyonu, bir pinin ne kadar süre HIGH veya LOW durumda kaldığını takip eder ve geçen süreyi mikrosaniye cinsinden döndürür.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Serial.print() fonksiyonunda gönderilen veri ekrana basılır ve aynı satırdan devam eder. Serial.println() fonksiyonunda ise gönderilen veri ekrana yazıldıktan 
sonra bir alt satıra geçerek yeni satırdan devam eder. Bir önemli nokta var, biz seri porta bilgi gönderirken, bilgileri karakter dizisi şeklinde göndeririz.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

digitalWrite ()
digitalWrite fonksiyonu daha önceden çıkış olarak ayarlanmış pinden güç çıkışı yapmak veya belirtilen pindeki gücü kesme işlemlerini yapar. 
İki parametre alır. İlk parametresi hangi pin olduğunu, ikinci parametresi ise gerilimin durumunu ayarlar.


*/




































































