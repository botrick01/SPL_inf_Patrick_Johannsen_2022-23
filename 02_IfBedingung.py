import random
random = random.Random()
randomint1 = random.randint(1, 100)
randomint2 = random.randint(1, 100)

print(randomint1)
print(randomint2)

if randomint1 < randomint2 and randomint1 < 50:
    print("Zahl1 ist kleiner als Zahl2 und mini")
elif randomint1 < 30 or randomint2 < 30:
    print("eine der beiden ist kleiner als 30")
elif randomint1 < 50 and randomint2 != 50:
    print("Erste Zahl klein, zweite kein 50iger") 