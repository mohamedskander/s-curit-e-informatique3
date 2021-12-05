# créeation d'un socket pour le client
import socket

host, port=('localhost', 5566)#127.0..0.1:adresse locale
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#(creation d' un socket)

try:
     socket.connect((host, port))
     print("client connéctée")
   
     

     data = "binvenue dans mon projet"
     data = data.encode("utf8")
     socket.sendall(data)
 
     
except ConnectionRefusedError:
    
     print("connexion au serveur échoué..")
finally:
     socket.close()
     
