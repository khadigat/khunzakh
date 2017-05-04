# the_best = []
# for i in range(1,10):
#     if i != 2:
#         the_best.append(i)
# print(the_best)

# the_best2 = [num for num in range(1,10) if num != 2]
# print(the_best2)

# animals = ['гусь', 'корова', 'собака']

# for num, animal in enumerate(animals):
#     print(num + 1, animal, end=" ")
# print()

# peoples = ['Арсен','Магомед','Омар','Андрей']

# for man, animal in zip(peoples,animals):
#     print(animal,'не', man)
from random import choice

def arsenRange(start,stop):
    names = ["Арсен","Андрей","Омар","Карим","Юнус"]
    for i in range(start, stop):
        yield choice(names)

for name in arsenRange(0,7):
    print(name)

