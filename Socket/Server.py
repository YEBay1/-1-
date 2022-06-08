import socket 

host="localhost"
port = 12345 

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket Oluşturuldu")
    
    s.bind((host,port))
    print("Socket {} nolu porta bağlandı".format(port))
    
    s.listen(5) 
    print("Socket dinleniyor")
   
except socket.error as msg:
    print("Hata",msg)
    
while True:
    c,addr=s.accept()
    print('Gelen bağlantı',addr)
    
    mesaj="Merhaba"
    c.send(mesaj.encode('utf-8'))
    
    c.close()



"""
 https://kerteriz.net/python-socket-programlama-nedir/
"""
