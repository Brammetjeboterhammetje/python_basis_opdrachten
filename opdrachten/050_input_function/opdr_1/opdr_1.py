# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.
from math import sqrt

lengte1 = int(input("Geef de lengte van de eerste zijde"))
lengte2 = int(input("Geef de lengte van de tweede zijde"))

antwoord = int(sqrt(lengte1**2 + lengte2**2))
print(antwoord)