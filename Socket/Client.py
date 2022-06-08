"""
Client tarafını yazarken ek olarak recv() fonksiyonu ile mesajın tampon boyutunu (buffer size) ayarlamamız gerekiyor.
Böylece bir sn de alınacak maksimum dosya boyutunu byte cinsinden ayarlamış oluyoruz.
Bu boyutu ayarlarken değerimizin 2 nin üssü şeklinde olmasına dikkat ediniz (Örneğin 1024, 2048, 4096…)
"""
import socket

# Socket oluşturulması
s = socket.socket()

# Bağlanılacak adres ve port
host = "localhost"
port = 15345            # Aynı port'a bağlan.Server'dan gelen mesajlar görülmeyebilir

try:
    # Bağlantıyı yap
    s.connect((host, port))

    # serverden yanıtı al
    yanit = s.recv(1024)
    print(yanit.decode("utf-8"))

    # bağlantıyı kapat
    s.close()
except socket.error as msg:
    print("[Server aktif değil.] Mesaj:", msg)




































