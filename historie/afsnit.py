class Afsnit:
    def __init__(self,overskrift,tekst,valg):
        self.overskrift = overskrift
        self.tekst = tekst
        self.valg = valg

    def udskriv(self):
        print()
        print("%%%% " + str(self.overskrift).upper() + " %%%%")
        print()
        print(self.tekst)
        print()
        taeller = 1
        valglabels = [""]
        for valglabel in self.valg.keys():
            print(str(taeller)+") "+self.valg[valglabel])
            valglabels.append(valglabel)
            taeller += 1
        return valglabels



