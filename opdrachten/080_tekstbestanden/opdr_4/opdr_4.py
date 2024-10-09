# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
lijst = []

vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank",
    "Wat neem je mee om te eten?"
]

for vragen in vragen:
    message = input(vragen + ": ")
    lijst.append(f"{vragen}: {message}\n")

with open('newtextt.txt', 'wt', encoding='utf-8') as fo:
    for entry in lijst:
        fo.write(entry)

print("Bedankt voor het invullen, fijne dag")