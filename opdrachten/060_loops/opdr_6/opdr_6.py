# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop


list = ["margharita", "calzone", "verdi", "olivio", "quattro stagioni"]

# Sorteer of alfabet
list.sort()
print(list)

# Voeg een pizza toe
list.append("Salami")
print(list)

# Verwijder een pizza
list.remove("verdi")
print(list)

# Print de eerste 3 van de lijst
print (list[:3])

# Print de middelste van de lijst
print (list[2])
# of
midden = len(list) // 2
print (list[midden])


# Print de laatste van de lijst
print(list[-3:])
# of (minder betrouwbaar)
print(list[2:])
