# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = [topping[0] for topping in toppings]

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

gevonden_topping = None
for topping in toppings:
    if keuze == topping[0]:
        gevonden_topping = topping
        break

if gevonden_topping:
    print(f"U heeft {gevonden_topping[0]} besteld, dat kost {gevonden_topping[1]}")
else:
    print("Er is een fout opgetreden")