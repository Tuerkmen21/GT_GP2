import random
zahl = random.randint (1,5)
i = 0
while i < 3:
    print ("zahl eingabe")
    feeling = input ()
    if feeling == zahl:
        print ("Glückwunsch du hast die richtige zahl gefunden")
    else :
        print ("schade versuche es noch einmal")
    i=i+1
    print (i)
print ("ich bin immernoch in der Schleife")
print("Wir sind aus der Schleife, da wir nun 10 mal durch sind")

