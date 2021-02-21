# her skrives "hei" til brukeren, brukeren må svare for å komme videre til neste del av koden, men det er ikke intuitivt å svare til "hei". a blir assigned som variabel til denne input'en.
a = input("hei")

# a blir gjort om til tallverdi. b blir assigned som variabel til int(a). 
b = int(a)

# hvis b er mindre enn 10, ønskes det at programmet printer b + Hei! Men her kommer det feilmelding fordi b er int og "Hei!" er str.
if b < 10:
    print (b + "Hei!")

# print (b + "Hei!") er ikke tillatt fordi vi prøver å slå sammen en tekststreng og et heltall. 
# vi møter på en feilmelding når koden blir kjørt.
# hvis vi setter "b" i stedenfor b, er det mulig å kjøre koden.