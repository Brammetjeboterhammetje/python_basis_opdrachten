# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

# Define the questions
questions = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind je de mooiste stad van Nederland?"
]

# Initialize the list to store answers
lst = []

# Loop through each question
for question in questions:
    message = input(question + ": ")
    lst.append(f"{question}\n{message}\n")

# Write the answers to a text file
with open('newtext.txt', 'wt', encoding='utf-8') as fo:
    for entry in lst:
        fo.write(entry + "\n")