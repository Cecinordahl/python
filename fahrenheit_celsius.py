# Et program som ber brukeren om en temperatur i Fahrenheit og konverterer denne til Celsius

#Spør brukeren om en temp i F
inp = input("Oppgi en temperatur i Fahrenheit: ")

#Variablene tempF og tempC får desimal tallverdi
tempF = float(inp)
tempC = float(inp)

#Skriver ut temp i F og temp konvertert til C
print("Temperatur i Fahrenheit", tempF)
tempC = ((tempF-32)*5/9)
print("Temperatur i Celsius", tempC)