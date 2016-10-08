from afsnit import Afsnit

class Historie:
    def __init__(self):
        self.afsnit = {}
        self.valgt_afsnit = ""

    def tilfoej_afsnit(self,titel,afsnit):
        if afsnit.__class__ == Afsnit:
            self.afsnit[titel] = afsnit

    def vaelg_afsnit(self,valg):
        if self.afsnit.__contains__(valg):
            self.valgt_afsnit = valg

    def skriv_afsnit(self):
        slutning = False
        valgt_afsnit = self.afsnit[self.valgt_afsnit]
        valgmuligheder = valgt_afsnit.udskriv()
        if len(valgmuligheder) > 1:
            afsnit_nummer = 0
            while afsnit_nummer < 1 or afsnit_nummer > len(valgmuligheder):
                afsnit_nummer = int(input("Hvad gør du?"))
            self.vaelg_afsnit(valgmuligheder[afsnit_nummer])
        else:
            print("SLUT")
            slutning = True
        return slutning


