# Opdracht 2 berekeningen
# Naam student:
# Groep:

# C = (F – 32) / 1,8 
# F = (C x 1,8) + 32

C1 = int(input("Hoeveel graden Celcius?"))
F1 = int(input("Hoeveel graden Fahrenheit"))
Naar_F1 = (C1 * 1.8) + 32
Naar_C1 = (F1 - 32) / 1.8


# Eerste Tempraturen
print(f"{C1}, graden Celcius is gelijk aan {Naar_F1:.1f} graden Fahrenheit")
print(f"{F1}, graden Fahrenheit is gelijk aan {Naar_C1:.1f} graden Celcius")