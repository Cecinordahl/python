


voksen = input("Er du voksen? (ja/nei): ")
gravid = input("Er du gravid? (ja/nei): ")

if voksen == "ja":
    if gravid == "nei":
        print("Velkommen til karusellen")
    else:
        print("Du kan ikke kjøre karusell når du er gravid")

else:
    print("Du må være voksen")
