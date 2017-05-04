import random

name = "Достоевский Федор. ИДИОТ - royallib.ru.txt"
with open(name, "rt", encoding="utf-8") as f1:
    text = f1.read()

# print(text)
input("Введите Ваш вопрос: ")

offset = 50
rand_number = random.randint(1,len(text) - offset)

answer = text[rand_number:rand_number + offset]

start = answer.find(" ")
stop = answer.rfind(" ")
answer = answer[start+1:stop]
print(answer)