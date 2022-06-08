"""
Ağdaki cihazlar arasında haberleşme sağlamak
Socket programlama, ağdaki iki farklı cihaz arasında TCP/IP protokülünü kullanarak IP ve port numaraları üzerinden bir kanal oluşturularak haberleşme yapılmasını sağlar.
Bu haberleşme de bir socket (uç cihaz,node) belirlenen IP ve port üzerinden kanalı dinlerken diğer socket (uç cihaz,node) aynı kanal üzerinden diğer uca erişmeye çalışır.
Bu bağlantıda server kanalı dinleyen uç, client ise servera ulaşmaya çalışan uçtur.

import socket

host = "127.0.0.1"  # localhost
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

Bu noktada socket(family, type) yapısındaki socket fonksiyonunda geçirdiğimiz iki parametreyi de açıklayalım:

family parametresi AF_UNIX, AF_INET ve AF_INET6 değişkenlerini alabilir.

AF_UNIX: UNIX domain protokolleri
AF_INET: TCP ve UDP için IPv4 protokolleri
AF_INET6: TCP ve UDP için IPv6 protokolleri
type parametresi SOCK_STREAM, SOCK_DGRAM, SOCK_RAW, SOCK_RDM ve SOCK_SEQPACKET değişkenlerini alabilir.

SOCK_STREAM: TCP bağlantı tipi
SOCK_DGRAM: UDP bağlantı tipi
SOCK_RAW: Henüz olgunlaşmamış soketler
SOCK_RDM: Güvenilir datagramlar için
SOCK_SEQPACKET: Bağlantı üzerinden kayıtlar için bir dizi transfer.

Biz bu örneğimizde en çok kullanılan TCP bağlantı tipini ve IPv4 adresleme seçeneğini kullanacağız. 
Bir önceki kodumuz ile bağlantıyıda hazır ettiğimize göre artık server kanalı dinlemeye hazır demektir.


s.listen(5)     # Aynı anda en fazla 5 bağlantı

"""
import socket

host = "localhost"
port = 15345

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket oluşturuldu")

    s.bind((host, port))
    print("socket {} nolu porta bağlandı".format(port))

    s.listen(5)
    print("socket dinleniyor")

except socket.error as msg:
    print("Hata:",msg)

while True:
   # Client ile bağlantı kurulursa
   c, addr = s.accept()
   print('Gelen bağlantı:', addr)

   # Bağlanan client tarafına hoşgeldin mesajı gönderelim.
   mesaj = "Merhaba"
   c.send(mesaj.encode('utf-8'))

   # Bağlantıyı sonlandıralım
   c.close()









































































