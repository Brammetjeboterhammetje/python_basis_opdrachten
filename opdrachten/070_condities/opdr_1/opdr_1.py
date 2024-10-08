# Opdracht 1 condities
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

nummers = []

# Loop die nummers vult met 1 tot 10
for x in range(1,11):
    nummers.append(x)

resultaat = [loop for loop in nummers if loop > 4]
print(resultaat)

#for loop
#if statement