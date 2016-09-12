#coding=utf8

# Når vores programmer bliver lidt mere komplicerede får vi rigtig mange variable
# Det gør at de bliver mere og mere besværlige at læse
# Nogle gange så hænger flere af de variable sammen
# Så kan vi prøve at lave dem om til en enkelt variabel som gemmer på mere end én ting ad gangen
# Den mest simple hedder en liste

minshoppingliste = ["1 kg mel","2 liter mælk","3 skumfiduser"]
print("Min shoppingliste lyder: "+str(minshoppingliste))

# Det ser ikke særlig pænt ud, men det er også ok
# Når vi bruger lister, så plukker vi enkelte ting ud ad gangen
# Det gør vi med at bruge firkantede parenteser
# minshoppingliste[<nummer>] giver os et element fra listen

print("Det første på listen er "+minshoppingliste[0])
print("Det tredie på listen er "+minshoppingliste[2])
print("Det andet på listen er "+minshoppingliste[1])

# Hov! Der står 2 hvor vi skal tage det tredie element
# Jep, den er god nok.  Computere tæller altid fra 0, så det kan vi lige så godt vænne os til

# Vi kan også bruge variable når vi vælger fra listerne:

nummer = 0

print("Element nummer "+str(nummer) + " på listen er: " + minshoppingliste[nummer])
print("")
# Prøv at lave om på "nummer" og se hvad der sker

# Vi kan også lave andre slags lister.  For eksempel "dict", som er en slags ordbog
# En dict er god til at gemme ting hvor rækkefølgen er ligegyldig
# I stedet for en firkantet parentes bruger vi en krøllet (Tuborg) parentes
# Hvert element i listen gemmes som en nøgle og en værdi med kolon imellem

mitfodboldhold = {"målmand" : "P. Schmeichel", "højre back" : "P. Ninkov", "angriber" : "C. Ronaldo"}

print("Holdets målmand er: "+mitfodboldhold["målmand"])
print("Holdets højre back er: "+mitfodboldhold["højre back"])
print("Holdets angriber er: "+mitfodboldhold["angriber"])
print("")

# Vi kan godt lave om på dele af holdet uden at starte forfra

mitfodboldhold["målmand"] = "J. Hart"

print("Holdets nye målmand er: "+mitfodboldhold["målmand"])
print("Holdets højre back er: "+mitfodboldhold["højre back"])
print("Holdets angriber er: "+mitfodboldhold["angriber"])
print("")

# Øvelse:  Lav en liste over jeres yndlingsbøger og print ud til skærmen
