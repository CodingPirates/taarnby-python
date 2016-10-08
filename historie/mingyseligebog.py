from historie import Historie
from afsnit import Afsnit

#### Alle afsnit ####

afsnit_indledning = Afsnit(
    "Det var en mørk og stormfuld aften",
    "Regnen siler ned, og du kan se lysglimt fra lynene i det fjerne.  Din bil er brudt sammen og du fryser. \n"
    + "Du bliver nødt til at finde dig noget nattely. Lidt længere ned ad vejen ser du et stort, gammelt hus \n"
    + "som står op på en bakketop. Der er lys i vinduet, så du går igennem den knirkende jernport og op til huset. \n"
    + "For enden af stien er der en stentrappe, og øverst på trappen er der en stor, solid dør.",
    {"ud_på_gaden": "Vender du om og går ud på gaden?",
     "bank_på": "Går du op til døren og banker på?"}
)

afsnit_tilbagetilgaden = Afsnit(
    "Du går tilbage på gaden",
    "Du kigger en sidste gang op på det uhyggelige hus og beslutter dig for at du hellere vil gå tilbage til \n"
    + "bilen og se om ikke der kommer nogen forbi.  Du er så lettet over din beslutning at du lægger ikke mærke \n"
    + "til det som kommer listende bag dig før det bider dig i halsen og trækker dig ud i mørket. Det var en skam. \n",
    {}
)

afsnit_bankpaadoeren = Afsnit(
    "Du banker på døren",
    "Du trækker vejret dybt og trækker i den tykke klokkestræng der hænger ved siden af den store egetræsdør. \n"
    +"En dyb gong lyder inde i huset og du hører tunge klonk-klonk-lyde som kommer nærmere.  Lydene stopper op \n"
    +"og døren åbner med en høj knirken. Indenfor står en pukkelrygget og skæløjet mand iklædt en mørk kutte. \n"
    +"\"Velkommen til Slot Frankenstein.  Mit navn er Igor.\"",
    {"spørg_igor": "Spørg Igor om hjælp?",
     "spørg_efter_frankenstein": "Bed Igor om at føre dig til sin mester?"}
)

afsnit_igorhjaelp = Afsnit(
    "Du beder Igor om hjælp",
    "\"Godt at se dig, Igor.  Min bil er brudt ned lidt længere ned ad vejen og jeg mangler hjælp til at få den igang\"\n"
    + "Igor kigger op på dig og svarer: \"Ikke mange siger de er glade for at se Igor.  Igor hjælper dig med at lave din bil\"\n"
    + "I går op ad vejen, finder bilen og finder ud af at der mangler strøm på batteriet.  Heldigvis har Igor et par startkabler \n"
    + "på sig, og ved at koble dem til den nærmeste lygtepæl får han ladet batteriet nok op, så du kan køre igen.  Du er næsten \n"
    + "sikker på at han har lavet det nummer før, men siger kun tak og kører videre.  Om to timer når du dit hotel og sover godt\n"
    + "efter nattens strabadser. Du fortæller historien flere gange efter du kommer hjem men ingen tror på dig.",
    {}
)

afsnit_optilfrankenstein = Afsnit(
    "Dr. Frankensteins laboratorium",
    "Igor fører dig ind i huset og op en stor vindeltrappe.  Ved toppen af trappen er der en dør, og bag døren ser du det \n"
    + "mest mærkelige laboratorium du nogensinde har set.  Underlige væsker bobler i glasbeholdere og der er masser af \n "
    + "gammeldags afbrydere og blinkende lamper.  Ved et arbejdsbord står en mand med hvidt strithår iklædt en kittel med et \n"
    + "gummiforklæde på maven. \"Velkommen til mit ydmyge hus.  Jeg er Doktor Viktor Frankenstein\".  Du forklarer ham dit problem, og \n"
    + "han beder Igor om at lave de nødvendige forberedelser.  I falder lidt i snak, og Dr. Frankenstein er meget imponeret \n"
    + "over din hjerne. Du er så optaget af at imponere doktoren at du ikke lægger mærke til når Igor lister om bag dig og slår \n"
    + "dig ned med en trækølle. Det var vist din hjerne han ville få fat i hele tiden...",
    {}
)



# Lav historien
minhistorie = Historie()
minhistorie.tilfoej_afsnit("indledning",afsnit_indledning)
minhistorie.tilfoej_afsnit("ud_på_gaden",afsnit_tilbagetilgaden)
minhistorie.tilfoej_afsnit("bank_på",afsnit_bankpaadoeren)
minhistorie.tilfoej_afsnit("spørg_igor",afsnit_igorhjaelp)
minhistorie.tilfoej_afsnit("spørg_efter_frankenstein",afsnit_optilfrankenstein)

minhistorie.vaelg_afsnit("indledning")
er_det_slut = False
while not(er_det_slut):
    er_det_slut = minhistorie.skriv_afsnit()