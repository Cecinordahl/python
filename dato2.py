# ikke fullført!!!!

import datetime

dato1 = input("Skriv inn en dato i formen YYYYMMDD")
d1 = date(dato1)

dato2 = input("Skriv inn en dato i formen YYYYMMDD")
d2 = date(dato2)


if d1 == d2:
    print("Samme dato")
elif d1 > d2:
    print("Dato nr to er eldst")
else:
    print("Første er eldst")

