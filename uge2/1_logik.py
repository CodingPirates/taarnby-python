### Logik ###

# Computere er gode til andre ting end beregninger.  Logik er en form for beregning, hvor man
# undersøger om en udtalelse er sand eller falsk.  Vi har faktisk en helt speciel type til denne
# slags beregninger:  En Boolean.  Sådan én har to mulige værdier, sand eller falsk
# (i Python hedder det: true eller false)

# Sammenligninger:
# Det mest simple logik er at sammenligne to tal
# Her kan vi bruger følgende
# Er a større end b:     a > b
# Er a mindre end b:     a < b
# Er a lig med b:        a == b    <-- Læg lige mærke til at vi har to lig-med tegn.  Hvad ville der ske hvis der kun var et enkelt?
# Er a forskellig fra b: a != b

# Lad os lige prøve en gang:

print("Sæt a lig med 3")
print("Sæt b lig med 5")
print("")

a = 3
b = 5

print("Er a større end b?")
print(a > b)
print("")

print("Er a mindre end b?")
print(a < b)
print("")

print("Er a lig med b?")
print(a == b)
print("")

print("Er a forskellig fra b?")
print(a != b)
print("")

# If-then-else
# Vi kan også gøre noget andet :  Vi kan lave en sammenligning, og så køre forskellige kommandoer afhængig af hvad der sker
# Til det bruger vi if-sætninger

if a > b:                                   # Hvis a er større end b, så:  (det er vigtigt at huske kolon
    print("Nu har vi sammenlignet a og b")  # Man kan godt køre flere end én kommando
    print("og a var rent faktisk større")   # Man skal bare huske at rykke dem ind (brug Tab-tasten)
elif a < b:                                 # elif står for "else if":  ellers, hvis
    print("Nu sammenlignede vi de to")
    print("og a kom ikke i nærheden af b")
else:                                       # Og til sidst, så kan man bruge else:
    print("Ved du hvad??")                  # Man behøver ikke, men man gør det hvis der skal ske noget uanset hvad
    print("De var skis'me lige store!")

