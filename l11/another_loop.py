i = 10
while i > 0: 
	i -= 1
	if i == 5:
		continue
		if i == 3:
			break
	print(i)
	# input()

animals = ["Собака", "Кошка", "Корова", "Осьминог"]

for animal in animals:
	if animal == "Осьминог":
		continue
	print(animal)
    
for i in range(0,6,2):
	print(i)

magomed = {
	"имя":"Магомед",
	"фамилия":"Тулиев"
}

for key in magomed:
	print(key,"-", magomed[key])

for key, value in magomed.items():
	print(key,":",value)