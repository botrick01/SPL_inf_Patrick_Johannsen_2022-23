print("Wählen Sie die gewünschte Funktion")
print("1. Einzahlen")
print("2. Abheben")
print("3. Kontostand")
print("4. Ende")

balance = 0

while True:
    selected = int(input())
    if(selected == 1):
        amount = int(input())
        balance += amount
        print("Sie haben " + str(amount) + "€ eingezahlt")
    elif(selected == 2):
        amount = int(input())
        balance -= amount
        print("Sie haben " + str(amount) + "€ abgehoben")
    elif(selected == 3):
        print("Der Kontostand beträgt " + str(balance) + "€")
    elif(selected == 4):
        break
