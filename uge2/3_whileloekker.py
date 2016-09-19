###  While-løkker  ###

# Det er ikke altid vi ved lige præcis hvor mange gange vi gerne vil køre løkken igennem
# Her kan vi kombinere en løkke og en sammenligning
# Hvis vores sammenligning er "True", så kører vi en gang til
# Hvis den er "False", så stopper vi

# Vi skal dog passe lidt på.
# Hvis man ikke tænker sig helt om med vores logik, så kan vi komme ud for at vi kører en uendelig løkke

# Verdens værste køretur:

kilometer_koert = 0

while kilometer_koert < 1000:
    print("Hvornår er vi der?!")

# Hvad var det lige vi glemte?  Jo, vi har ikke husket at starte bilen...kilometer_koert er altid lig nul!

# Vi prøver lige én gang til:

kilometer_koert = 0

while kilometer_koert < 1000:
    print("Hvornår er vi der!?")
    kilometer_koert = kilometer_koert + 1

