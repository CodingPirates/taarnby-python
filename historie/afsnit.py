class Afsnit:
    def __init__(self,overskrift,tekst,valg):
        # Vi skal bruge tre ting, en overskrift til afsnittet, noget tekst og nogle valg
        # Overskrift og tekst er strenge, ingen hokus-pokus der
        # Valg er en dict hvor vi laver en liste med valgmuligheder.  Nøglen bruger vi til at kæde
        # de forskellige afsnit sammen, og værdien er den tekst der bliver skrevet ud
        # Eksempel: {"gå_tilbage": "Vil du gå tilbage?", "gå_frem": "Vil du tage dig sammen og fortsætte"}
        self.overskrift = overskrift
        self.tekst = tekst
        self.valg = valg

    def udskriv(self):
        # Først skriver vi overskriften med nogle procenttegn før og efter
        # funktionen upper() laver vores streng om til store bogstaver
        print()
        print("%%%% " + str(self.overskrift).upper() + " %%%%")
        print()
        # Bagefter skriver vi vores tekst, og tilføjer en tom linie
        print(self.tekst)
        print()
        # Nu skal vi skrive alle valgmulighederne ud.  Mens vi gør det, så laver vi en liste
        # med alle valgmulighederne og sender tilbage.  Klassen "Afsnit" ved ikke hvor vi går hen
        # i historien, det bliver håndteret i klassen "Historie", og derfor sender vi valgene tilbage
        taeller = 1
        # Her laver vi vores liste med valgmuligheder.  Vi sætter en tom streng ind som det første element
        # fordi vi tæller ikke fra 0 lige som Python gør.
        valglabels = [""]
        # Vi laver en løkke som går igennem alle nøgler i vores dict (husk, en dict består af {nøgle: værdi, nøgle2: værdi2, ...}
        for valglabel in self.valg.keys():
            # Vi printer et nummer med parentes bag (en optælling) og så tager vi dict med valg og slår den rigtige tekst op
            print(str(taeller)+") "+self.valg[valglabel])
            # Tilføj etiketten til listen
            valglabels.append(valglabel)
            # Og husk at tælle op :)
            taeller += 1
        # Når vi er færdige sender vi etiketterne tilbage
        return valglabels



