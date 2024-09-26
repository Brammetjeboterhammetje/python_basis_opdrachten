# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

# Maak een dictionary met een aantal grote rivieren

rivieren = list(rivier_info.keys())




##################

# Print de naam van de 1e rivier
print(f"De naam van de eerste rivier is {rivieren[0]}")

# Print het 2e land waar de 1e rivier doorheen stroomt 
print(rivier_info['rijn'][1].capitalize(), "Stroomt door de", (rivieren[0].capitalize()))
# of
print(rivier_info[rivieren[0]][1].capitalize(), "Stroomt door de", (rivieren[0].capitalize()))
# of
print(f"{rivier_info[rivieren[0]][1].capitalize()} Stroomt door de {rivieren[0].capitalize()}")

###################

# Print de naam van de 2e rivier
print(f"De naam van de 2e rivier is {rivieren[1]}")

# Print het 1e land waar de 1em rivier doorheen stroomt 
print(rivier_info["maas"][2].capitalize())
# of
print(rivier_info[rivieren[1]][2].capitalize(), "loopt door de", (rivieren[1].capitalize()))
# of
print(f"{rivier_info[rivieren[1]][2].capitalize()} loopt door de {rivieren[1].capitalize()}")

#######################



