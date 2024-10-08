# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

try:
    leeftijd_persoon = int(input("Geef uw leeftijd in aantal jaren"))
except ValueError:
    print("Input moet een leeftijd zijn")


def bepaal_groep(leeftijd_persoon):
    if 0<= leeftijd_persoon <=2:
        return "baby"
    elif 3<= leeftijd_persoon <=18:
        return "kinderen"
    elif 19<= leeftijd_persoon <=64:
        return "volwassenen"
    elif 65<= leeftijd_persoon <=150:
        return "ouderen"
    else:
        print("Vul een realistische leeftijd in")
        return None
    

leeftijdsgroep = bepaal_groep(leeftijd_persoon)
korting = kortings_percentages[leeftijdsgroep]
te_betalen = normale_toegangsprijs * (1 - korting / 100)

print(f"U behoort tot de groep {leeftijdsgroep}")
print(f"U krijgt {korting}% korting")
print(f"U betaalt daarom {te_betalen:.2f}")