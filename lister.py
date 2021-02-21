#lager lister

liste1 = [1, 2, 3]
liste1.append(5)
print(liste1[0], liste1[2])

liste2 = []

print("Oppgi fire navn")

n1 = str(input("1. "))
liste2.append( str(n1) )
n2 = str(input("2. "))
liste2.append( str(n2) )
n3 = str(input("3. "))
liste2.append( str(n3) )
n4 = str(input("4. "))
liste2.append( str(n4) )
if n1 or n2 or n3 or n4 == "cecilie":
    print("Du husket meg!") 
else:
    print("Glemte du meg?")


print(liste2)