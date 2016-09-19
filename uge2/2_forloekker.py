### For-løkker ###

# En anden ting som computere er gode til er at gentage sig selv
# De bliver aldrig trætte af at lave det samme hele tiden...lidt ligesom en guldfisk!

# Der findes to slags løkker:
# Den første slags bruger man når man ved hvor mange gange man vil køre
# Den hedder en for-løkke


# Vi vil gerne tælle fra 1 til 10:

for tal in range(1,10):                                 # range(1,10) laver en liste med tal fra 1 til 10
    print("Vi tæller, og vi er nået til: " + str(tal))  # Vi printer ud
print("Nu er vi færdig med at tælle")                   # <== Se her!  Når linien rykker tilbage til starten af linien, så er den ikke med i løkken
print("")

#  Vi kan også lave noget andet.  Kan du huske lister?
# Vi laver en liste med alle linierne fra sidste vers i "Bro Bro Brille"

bro_bro_brille = ["Første gang så la'r vi ham gå,", "anden gang så lige så,", "tredie gang så ta'r vi ham", "og putter ham i gryden!"]

# Så i stedet for at printe alle linierne ud på hver sin linie....så gør vi det på en simplere måde:

for linie in bro_bro_brille:
    print(linie)


