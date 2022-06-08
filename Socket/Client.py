import socket 

s=socket.socket()

host="localhost"
port = 12345 

try:
    s.connect((host,port))
    
    yanit=s.recv(1024)
    print(yanit.decode("utf-8"))
    
    s.close()
    
except socket.error as msg:
    print("[Server aktif değil] Mesaj:",mgs)
    


"""
 https://kerteriz.net/python-socket-programlama-nedir/
"""
