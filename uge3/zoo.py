from dyr import *

# I filen dyr.py er der defineret nogle klasser med forskellige dyr
# I vores hovedprogram (zoo.py) så laver vi nogle specifikke dyr
# Det kaldes objekter (vi har objektet "mikkel" af klassen "ræv" for eksempel)

# Lad os først lave et mutantdyr
mutantdyr = Dyr("Mutantdyr","slim","rawr","små børn",4,False)
mutantdyr.hvem_er_jeg()
mutantdyr.spisetid()
print("")


# Vi har fundet Nemo!
nemo = Guldfisk("Nemo")
nemo.hvem_er_jeg()
nemo.spisetid()
print("")

# Hvad var det nu ræven sagde igen?
mikkel = Raev("Mikkel")
mikkel.hvem_er_jeg()
mikkel.spisetid()
print("")


# Kender I Aristocats?
thomasomalley = Kat("Thomas O'Malley")
duchess = Kat("Duchess","Angora")

thomasomalley.hvem_er_jeg()
thomasomalley.spisetid()
print("")
duchess.hvem_er_jeg()
duchess.spisetid()
duchess.spind()

# Nu prøver vi noget, til allersidst:  Kan vi ikke få en guldfisk til at spinde?
nemo.spind()

# I kan godt se at det giver fejl, ikke?

# Opgave:  Lav en klasse der hedder "Hest".  Hesten skal kunne springe over en vilkårlig forhindring og stejle
# Hint:  lav funktionerne spring(forhindring) og stejl().  Brug print funktionen til at printe en sjov beskrivelse
