import random

sum = 0
randomint = random.randint(10, 30)

while randomint != 15 and randomint != 25:
    sum += randomint
    randomint = random.randint(10, 30)

print(sum)