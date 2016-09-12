#coding=utf8

# Nogle gange så kan vi ikke vide alt på forhånd
# Derfor så skal vi kunne bede den der bruger vores program om at skrive noget til os
# Når vi skriver til skærmen, hedder det output.  Så det vi skal bruge her, er det omvendte: input

svar = input('Skriv noget til mig: ')
print("Du skrev: "+svar)
print("")

# Vi prøver lige at samle to tal sammen

tal1 = input("Første tal: ")
tal2 = input("Andet tal: ")
print("Første tal plus andet tal er lig med "+str(tal1+tal2))
print("")

# Hov! Hvad er nu det for noget?
# Nåh, jo.  Det vi får tilbage er strenge, og ikke tal
# Vi kan få Python til at lave vores svar om til tal ved at bruge eval() kommandoen

print("Eval: Første tal plus andet tal er lig med "+str(eval(tal1)+eval(tal2)))

# Øvelse:  Lav et program der spørger om dit navn og din alder, og skriver ud til skærmen