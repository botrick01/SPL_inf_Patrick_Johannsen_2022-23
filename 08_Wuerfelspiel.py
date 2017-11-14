import random

round = 1
sumPlayer = 0
sumComputer = 0

print("Welcome to THE GAME, press Enter to start")

while round <= 6:
    if(input() == ""):
        print("Round " + str(round))
        playerWurf = random.randint(1, 6)
        sumPlayer += playerWurf
        print("Du hast eine " + str(playerWurf) + " geworfen")
        computerWurf = random.randint(1, 6)
        sumComputer += computerWurf
        print("Der Computer hat eine "+ str(computerWurf) + " geworfen")
        round += 1

print("Endstand: " + str(sumPlayer) + " - " + str(sumComputer))

if(sumPlayer > sumComputer):
    print("Congrats, you have won!")
else:
    print("Oh no, you lose... maybe next time")