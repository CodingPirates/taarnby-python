#coding=utf8

# Indtil videre har vi været flittige og skrevet en masse ting ud til skærmen
# Indtil videre har det været nogle faste tal og strenge som vi har skrevet ud
# Nogle gange så ved man ikke helt hvad man vil skrive til skærmen før man kører programmet
# For eksempel, hvis man vil regne videre på nogle udregninger man lavede før
# Hvis vi skriver regnestykkerne ind direkte skal vi rette i alle de efterfølgende
# Det synes vi er lidt spildarbejde.  Derfor findes der noget der hedder "variable"

# Variable er lidt ligesom skuffer med en etiket på.  Hvis man vil se hvor mange skruer man har,
# så åbner man skuffen hvor der står "skruer" og tæller

skruer = 9
print("Vi åbnede skuffen og talte "+str(skruer)+" skruer")
print("")

# Variable kan godt ligne strenge lidt når man først ser dem
# Forskellen er at man ikke har gåseøjne omkring variable

# Vi kan godt lægge variable sammen.  Hvis vi har 12 møtrikker, hvor mange skruer og møtrikker har vi så sammenlagt

motrikker = 12
skruer_og_motrikker_sammenlagt = skruer+motrikker

print("Vi har sammenlagt "+str(skruer_og_motrikker_sammenlagt) + " skruer og møtrikker")
print("")

# Læg mærke til at vi huskede hvor mange skruer vi havde fra før
# Hvad nu hvis vi ændrede antal skruer og printede ud igen

skruer = 14
print("Med 14 skruer har vi har sammenlagt "+str(skruer_og_motrikker_sammenlagt) + " skruer og møtrikker")
print("")

# Åh hvad?? Det er forkert! 14 skruer og 12 møtrikker giver jo 26 i alt!
# Men det er der jo en forklaring på.  Computeren kan jo ikke læse tanker
# Den forstår heller ikke hvad variablen "skruer_og_motrikker_sammenlagt" betyder
# Derfor skal vi huske at hvis vi ændrer på en variabel, så skal vi regne det hele fortfra

# Nu opdaterer vi skruer og møtrikker sammenlagt:
skruer_og_motrikker_sammenlagt = skruer+motrikker
print("Når vi har opdateret har vi har sammenlagt "+str(skruer_og_motrikker_sammenlagt) + " skruer og møtrikker")
print("")

# Det var bedre

# Varible kan være andet end tal, en streng kan sagtens være variabel

mit_navn = "Ragnar"
print("Hej, jeg hedder " + mit_navn + ", jeg arbejder i kassefabrikken." )