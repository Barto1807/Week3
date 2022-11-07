def quadrato(): #Funzione per calcolare il perimetro del quadrato
	print ("\nCalcoliamo il perimetro del quadrato\n")
	x= int (input("Inserisci lunghezza lato: "))	# variabile per inserire il lato
	y = x ** 2	#variabile per calcolare il perimetro del quadrato
    	print(" Il perimetro e': ",y)

def cerchio(): #Funzione per la circonferenza del cerchio
	print ("\nCalcoliamo la circonferenza del cerchio\n")
    	raggio = int (input("Inserisci lunghezza raggio: "))	# variabile per inserire il raggio
    	print ("La circonferenza e': ",2*3.14*raggio) # insieme al print c'è anche la variabile per calcolare la circonferenza

def rettangolo(): #Funzione per il perimetro del rettangolo
	print ("\nCalcoliamo il perimetro del rettangolo\n") 
   	base = int (input("Inserisci lunghezza base: "))	# variabile per inserire la base
    	altezza = int (input ("Inserisci lunghezza altezza: "))	# variabile per inserire l'altezza
	perimetro = (base+altezza)*2	# variabile per calcolare il perimetro
    	print ("Il perimetro del rettangolo e': ",perimetro)

while 1==1: #Il while è usato per ripetere ogni volta il menu' di scelta

	print ("\nBenvenuto, qui possiamo calcolare il perimetro di alcune figure geometriche\n")
	scelta = int(input("Per il quadrato premi 1\nPer il cerchio premi 2\nPer il rettangolo premi 3\nPer uscire premi 4\n"))
	
	if (scelta == 1):	# if-else usato per indirizzare su una delle scelte
        	quadrato()
    	
	elif (scelta == 2):
        	cerchio()
    	
	elif (scelta == 3):
        	rettangolo()
    	
	elif (scelta == 4):
        	print("Arrivederci")
       	quit()
    
	else:
        print("QUADRATO 1\nCERCHIO 2\nRETTANGOLO 3\nUSCITA 4\n")
        

