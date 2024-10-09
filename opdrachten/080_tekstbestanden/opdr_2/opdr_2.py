# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
getal = random.randint(1, 100)
pogingen = 0

while True:
    poging = input("Raad het getal: ")

    if (poging.lower()) == "stop":
        print(f"Het getal was {getal}.")
        print(f"Je hebt {pogingen} pogingen gedaan.")
        exit()    
    try:
        poging = int(poging)
    except ValueError:
        print("Voer een geldig getal in.")
        continue

# Getal dat niet klopt 
    if poging < 0 or poging > 100:
        print("Het getal moet tussen 0 en 100 liggen.")
        print("Start het programma opnieuw op")
        exit ()

    pogingen += 1

# Getal klopt
    if poging == getal: 
        print(f"Je hebt het getal geraden in {pogingen} pogingen.")
        break


# Als het getal hoger is
    if poging < getal:
        print("Het getal is hoger.")
# Als het getal lager is
    if poging > getal:
        print("Het getal is lager.")

    