import random
import math
from math import ceil, trunc
# from random import *
from random import randint
import syntax


print(math.sqrt(4))
print(ceil(4.8))
print(trunc(4.8))
print(randint(1,5))
print(random.choice(["1",5,"4"]))

word = input("Введите слово: ")
syntax.show_wrong(word)