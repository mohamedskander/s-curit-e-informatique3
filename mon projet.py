import random
import socket
print ("bienvenue dans mon projet ");
T= ("a","c","d","3","4","r","o","m");
L= ["a","b","c","d"]
x1 = str(input("choisir un caractére parmi les carctéres suivant a,b,c,d") )
x2 = str(input("choisir un caractére parmi les carctéres suivant a,b,c,d") )
x3 = str(input("choisir un caractére parmi les carctéres suivant a,b,c,d") )
x4 = str(input("choisir un caractére parmi les carctéres suivant a,b,c,d") )
x5 = str(input("choisir un caractére parmi les carctéres suivant a,b,c,d") )
x6 = str(input("choisir un caractére parmi les carctéres suivant a,b,c,d") )

if (x1!="a") and (x1!="b") and (x1!="c") and (x1!="d") or (x2!="a") and (x2!="b") and (x2!="c") and (x2!="d") or (x3!="a") and (x3!="b") and (x3!="c") and (x3!="d") or (x4!="a") and (x4!="b") and (x4!="c") and (x4!="d") or (x5!="a") and (x5!="b") and (x5!="c") and (x5!="d") or (x6!="a") and (x6!="b") and (x6!="c") and (x6!="d"): 
     print("erreur")
else:
    x1 = random.randint(0,7)  
    x2 = random.randint(0,7)
    x3 = random.randint(0,7)
    x4 = random.randint(0,7)
    x5 = random.randint(0,7)
    x6 = random.randint(0,7)
    mdp = [T[x1],T[x2],T[x3],T[x4],T[x5],T[x6]]
    mdp = ",".join(mdp)
    motdepasse =mdp
    print( "le mot de passe est:",motdepasse)
    message =input("taper votre message a envoyer svp")
    mdp1 =input("pour ouvrir le message veuiller taper le mot depasse correcte")
    if mdp==mdp1:
        
        print("votre message est",message)
    else:
        print("erreur")
















        

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
#remarque le serveur et le client nécessite un terminale pour démarrer  


 
 
