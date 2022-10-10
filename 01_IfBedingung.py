import random
random = random.Random()
randomint = random.randint(1, 100)
print(randomint)
if randomint<20:
    print("mini")
elif randomint<50:
    print("medium")
else:
    print("large")