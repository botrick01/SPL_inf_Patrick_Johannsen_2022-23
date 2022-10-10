import random

def add(num1, num2):
    return num1 + num2

def randomInt():
    randomint = random.randint(100, 200)
    return randomint

def randomWord(array):
    return random.choice(array)

print(add(3, 7))
print(randomInt())
print(randomWord(["hello", "servus", "gruezi"]))