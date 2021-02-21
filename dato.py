# Oppgave 3: Problemløsning med beslutninger

# Program som spør om og sammenlikner datoer ihht rekkefølge
# Jeg kunne sikkert gjort det på en enklere måte?



# --------------------------------------------
# Ber brukeren skrive inn datoer

dato1 = input("Skriv inn en dato i formen DD")
måned1 = input("Skriv inn en måned i formen MM")
dato2 = input("Skriv inn en ny dato i formen DD")
måned2 = input("Skriv inn en ny måned i formen MM")


# --------------------------------------------
# Programmet skriver ut en kommentar til bruker ihht om de har skrevet inn datoene i riktig rekkefølge

if måned1 > måned2 :
    print("Feil rekkefølge")
elif måned2 > måned1 :
    print("Riktig rekkefølge")
elif måned1 == måned2 and dato1 > dato2 :
    print("Feil rekkefølge")
elif måned1 == måned2 and dato2 > dato1 :
    print("Riktig rekkefølge")
elif måned1 == måned2 and dato1 == dato2 :
    print("Samme dato!")