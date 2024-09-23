import random
zahl = random.randint (1,5)
print(zahl)
i = 0
while True :
         try:
             print("zahl eingabe")
             feeling = int(input ())
             if feeling == zahl:
                print ("Glückwunsch du hast die richtige zahl gefunden")
                break
             else :
                print ("schade versuche es noch einmal")
         except: 
             print ("etwas ist Schief gelaufen")
    