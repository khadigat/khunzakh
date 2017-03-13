import random
random_number = random.randint(1,10)
answer = "2 * " + str(random_number) + "="
number = int(input(answer))
# print(number)
if number == 2 * random_number:
	print("Ответил верно")
else:
	print("Ты ошибся")