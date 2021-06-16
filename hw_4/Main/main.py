from hw_4 import Calculator
import random


def rand_list():
    rand_list = []
    while len(rand_list) < 20:

        r = random.randint(1, 100)
        if r not in rand_list:
            rand_list.append(r)
    return rand_list

random1 = random.choice(list(rand_list()))
random2 = random.choice(list(rand_list()))

print(random1, random2)

c = Calculator

Calculator.additions(random1, random2)
Calculator.subtract( random1,  random2)
Calculator.multy( random1,  random2)
Calculator.divide( random1,  random)

Calculator.additions(51,51,5,15,5,15,1,51,5,15,1,5)