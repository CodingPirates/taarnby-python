### Funktioner ###

# Vi har set nogle funktioner i brug før, f.eks. range som vi brugte lige før.
# Du kan godt lave din helt egen funktion.  Det kan være en god idé hvis
# du har lavet noget kode som skal køres mange steder i dit program.
# For det første sparer man plads, og for det andet skal man kun rette sin funktion ét sted
# hvis man finder ud af en bedre måde at programmere sin kode på!

# Vi skal lige bruge et eksempel.  Du skal lave en funktion der trækker 4 fra et tal.  Vi kalder det traek_fire


def traek_fire(tal):    # "tal" i parentesen kalder vi argumentet
    return tal-4


vores_tal = 8
print("Vores tal er ")
print( vores_tal )
print("")
print("Vores tal minus fire er ")
print( traek_fire(vores_tal) )
print("")

#  Vi kan også lave en funktion som har mere end ét argument:


def traek_tal(tal,traek):
    return tal-traek


vores_tal = 7
vores_traek = 5
print("Vores tal er ")
print( vores_tal )
print("")
print("Vores tal minus "+str(vores_traek) +" er ")
print( traek_tal(vores_tal,vores_traek) )

# Normalt ville vi lave en separat fil med vores funktioner, som vi så fortæller vores program at skal bruges 


