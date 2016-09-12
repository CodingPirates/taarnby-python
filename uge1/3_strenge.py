#coding=utf8

# Computere er rigtig gode til at huske tal
# Det er faktisk det eneste de er gode til
# Når de skal huske bogstaver, ord og sætninger husker de dem også som tal (f.eks. hvor a er lig med 1, b er lig med 2 osv)
# Enkelte bogstaver kaldes karakter
# Ord, sætninger og paragraffer huskes som en række tal
# Disse talrækker kaldes for strenge

# Det er ret strengt at skulle huske en masse tal i hovedet når man vil skrive noget i sit program
# Derfor så hjælper Python os med at gøre det.  Alt det vi skriver inde imellem to gåseøjne (") bliver lavet om til streng

print("Dette her er en streng")
print("")

# Vi kan også tage to strenge og lægge sammen.  Her bruger vi plustegnet

print("Nu tager vi en streng" + " og lægger sammen med en anden streng")
print("")

# Vi kan ikke sætte en streng og et tal sammen:
print("Antallet af fejl i denne streng er "+1)
print("")

# Hvis vi skal printe tal ud sammen med en streng, er det nemmest at lave tallet om til en streng hvor tallet står først
# Prøv at udkommentere (skriv # forrest i linien) kommandoen med fejl i
print("Antallet af fejl i denne streng er " +str(0))
print("")

# Funktionen "str" tager et tal, og laver den om til en streng.  Tallet 0 bliver til "0", tallet 1 bliver til "1" osv.

# Øvelse:  Print en streng ud til skærmen