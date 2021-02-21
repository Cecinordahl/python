# Oppgave 1: Utskrift og innlesning med variabler


# --------------------------------------------
# Spør brukeren om navn, bruker skriver inn navn, programmet sier hei tilbake

print("Hei student!")
navn = input("Hva heter du?")
print("Hei", navn)


# --------------------------------------------
# Kalkuleringer, finner differansen mellom to tall

tall1 = 50
tall2 = 20
tall3 = tall1 - tall2
print("Differanse:", tall3)


# --------------------------------------------
# Setter sammen to navn

print("Hei igjen, oppgi et nytt navn")
navn2 = input("Skriv inn nytt navn her")

sammen = navn + navn2
print(sammen)

sammen = navn + " " + "og" + " " + navn2
print(sammen)