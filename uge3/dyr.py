# Her laver vi en ny klasse.  Bemærk at vi altid laver klassenavne med et stort bogstav
class Dyr:
    # Her kommer nogle variable der tilhører klassen.  Alle objekter af samme klasse deler disse
    dyrtype = "dyr"

    # Her kommer initialiseringsfunktionen.  Den køres hver gang vi laver et nyt objekt af denne klasse
    # Vores klasse skal kunne lave al slags dyr, og derfor er der mange argumenter
    def __init__(self, navn, skind, lyd, foede, antal_ben, hvirveldyr):
        # "self" betyder "mig selv".  Når man siger self.antal_ben = 2, så sættes antal hjul til 2 for lige præcis
        # dette her objekt.  Andre objekter af samme klasse kan have en helt andet antal ben
        self.navn = navn
        self.antal_ben = antal_ben
        self.skind = skind
        self.hvirveldyr = hvirveldyr
        self.lyd = lyd
        self.foede = foede

    def hvem_er_jeg(self):
        print("Jeg er en "+self.dyrtype+" som hedder "+self.navn+". Jeg er dækket med "+self.skind+", har "+str(self.antal_ben)+" ben og jeg siger "+ str(self.lyd))
        if self.hvirveldyr == True:
            print("Jeg er et hvirveldyr")
        else:
            print("Jeg er ikke et hvirveldyr")

    def spisetid(self):
        print("Omnom, jeg spiser "+self.foede)

# Dyr er en basisklasse, men vi kan godt lave nogle mere specialiserede klasser
# Det er ingen grund til at opfinde den dybe tallerken en gang til
# Vi laver en mere simpel "init" funktion, fordi alle guldfiske har 0 ben og spiser larver.
# De har heller ikke noget navn. Derfor er det supersimpelt
class Guldfisk(Dyr):
    dyrtype = "guldfisk"

    def __init__(self,navn):
        Dyr.__init__(self, navn, "skæl", "ikke noget", "larver", 0, False)

# Nu kan vi lave en lidt mere avanceret dyr
# Alle hunde har 4 ben, pels og siger vov, men de har også nogle navne
class Raev(Dyr):
    dyrtype = "ræv"

    def __init__(self,navn):
        Dyr.__init__(self, navn, "pels", "wa pa pa pa pa pa pow", "mus", 4, True)

    # Hvis vi synes funktionerne fra moderklassen ikke er helt dækkende kan vi lave nogle nye
    # Det hedder at "override" funktionen.  Hvis man har et objekt af typen "Ræv" er det den der køres:
    def spisetid(self):
        print("Jeg kan rigtig godt lide at jage "+self.foede+" i skoven. Mums!")

# Vi skal da også have katte.  Udover at have navn, så kan de også have en race.  Hvis ikke vi angiver
# en race, så er de et "gadekryds"
class Kat(Dyr):
    dyrtype = "kat"

    # Vi har noget ekstra information som giver mening når vi har katte
    def __init__(self,navn,race="gadekryds"):
        Dyr.__init__(self, navn, "pels", "miauw", "kattemad", 4, True)
        self.race = race

    # Vi overrider "hvem er jeg", fordi vi har noget ekstra information (race)
    def hvem_er_jeg(self):
        print("Jeg er en " + self.race + "-kat som hedder " + self.navn + ". Jeg er dækket med " + self.skind + ", har " + str(
                self.antal_ben) + " ben og jeg siger " + str(self.lyd))

    # Katte kan spinde, men det giver ikke rigtig mening for de andre dyr
    # Vi kan godt lave funktioner som ikke er i moderklassen (her laver vi en "spind" funktion
    def spind(self):
        print("Rrrrrrrrrrrrr")

