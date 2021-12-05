# créeation d'un socket pour le serveur
import socket

host, port=('', 5566)

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#AF_INET,sock_STREAM:deux famills de sockets(creation d' un socket)
socket.bind((host, port))#host:l'adresse,port:numero de port de serveur car certain port sont reéservé par le serveur.le serveur va écouter sur le port 5566
print("le serveur est démarrer...")

while True:
     socket.listen(5)#le serveur autosrise 5 FOIS la connexion  avant que le serveur refuse d'autre connexion supplémentaire(ce champ n'est pas obligatoire por la version python au min 3.5.1.  
     conn, address=socket.accept()#il faut accépter la connexion .
     print("un client va se connecter...")

     data = conn.recv(1024)
     data =data.decode("utf8")
     print(data)
     
conn.close()
socket.close()


 
