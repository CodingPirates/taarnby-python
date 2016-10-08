from afsnit import Afsnit

class Historie:
    def __init__(self):
        # Klassen Historie skal holde styr på hele historien
        # Vi har en dict hvor vi gemmer vores afsnit, og hvert afsnit har en etiket
        # Etiketten bruges når man i sit valg vil over til det afsnit
        # Vi har også en variabel som husker hvilket afsnit er valgt lige nu
        self.afsnit = {}
        self.valgt_afsnit = ""

    def tilfoej_afsnit(self,titel,afsnit):
        # En funktion som tilføjer et afsnit til vores dict (self.afsnit).
        # Hvis ikke parameteren "afsnit" er af den rigtige klasse sker der ikke noget
        if afsnit.__class__ == Afsnit:
            self.afsnit[titel] = afsnit

    def vaelg_afsnit(self,valg):
        # Her vælger vi et nyt afsnit fra listen
        # Hvis det ønskede afsnit ikke findes på listen sker der ikke noget
        if self.afsnit.__contains__(valg):
            self.valgt_afsnit = valg

    def skriv_afsnit(self):
        # Vi skriver afsnittet ud til skærmen
        # Vi vil gerne se om det er det sidste afsnit, og der bruger vi variablen "er_det_slut_nu"
        er_det_slut_nu = False
        # Vi læser det valgte afsnit ud fra listen
        valgt_afsnit = self.afsnit[self.valgt_afsnit]
        # Vi henter valgmulighederne fra afsnittet
        valgmuligheder = valgt_afsnit.udskriv()
        # Hvis der er 1 eller flere valgmuligheder så (der er altid mindst én mulighed, som er tom og har nummer 0)
        # Derfor står der >1 og ikke >=1
        if len(valgmuligheder) > 1:
            # Sæt det valgte afsnit nummer til 0, vi har ikke valgt endnu
            afsnit_nummer = 0
            # Vi looper mens det valgte afsnitnummer ikke er mellem 1 og antal valgmuligheder
            while afsnit_nummer < 1 or afsnit_nummer > len(valgmuligheder):
                # Vi spørger brugeren hvilket valg han tager
                afsnit_nummer = int(input("Hvad gør du?"))
            # Når vi har valgt et gyldigt tal, så vælger vi det næste afsnit
            self.vaelg_afsnit(valgmuligheder[afsnit_nummer])
        else:
            # Hvis der ikke er nogle valgmuligheder er det en slutning på historien
            # Vi printer "SLUT" ud til skærmen så spilleren ikke er i tvivl
            print("SLUT")
            er_det_slut_nu = True
        # Hovedprogrammet skal have at vide at historien er slut
        return er_det_slut_nu


