# Lag en quiz hvor du spør brukeren om et par forskjellige spørsmål.
# Bruk if/else til brukeren's svar.

#Et spørsmål skal du bruke true/false. Spør brukeren om et true/false statement og skriv koden slik at brukeren har mulighet til å skrive sant/usant med store eller små bokstaver.
print("Velkommen til Quiz! Første spørsmål er sant eller usant.\n")
print("Isbjørnen liker kake")
svar1 = input("Sant eller usant?")

sant = ("sant")
usant = ("usant")

if svar1.lower() == sant:
    print("Riktig!")
elif svar1.lower() == usant:
    print("Feil :-(")

#Et spørsmål skal gi brukeren valgmuligheter. Gi brukeren mulighet til å skrive inn den riktige valgmuligheten på forskjellige måter.
print("\nNeste spørsmål...\n")
print("Hva er hovedstaden i Frankrike?")
print("a) Oslo\nb) Paris\nc) Reykjavik?")

svar2 = input("Skriv inn ditt svar: ")
paris = ("paris")
b = ("b")

if svar2.lower() == paris:
    print("\nRiktig!")
elif svar2.lower() == b:
    print("\nRiktig!")
else:
    print("\nFeil :-(")