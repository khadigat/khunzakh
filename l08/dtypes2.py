# name = "123456"
# print(name[3:4])
# text = '''много слов
# много слов
# много слов'''
# print(text.upper())
# text = text.upper()
# print(text.replace("МНОГО","мало"))

# list - списки

pupils = ["Магомед", "арсен", "Гаджикурбан", 94]
print(pupils)
print(pupils[1])
print(pupils[1:3])
pupils.append("Хадижат") #  Добавить в конец
print(pupils)
pupils.insert(1,"Рабадан") # Добавить
print(pupils)
some_peoples = ["Абакар", "Карим"]
pupils.extend(some_peoples) # расширить другим списком
print(pupils)
pupils[0] = "Супер Магомед" # Заменить
print(pupils)
del pupils[3] # удалить по индексу
print(pupils)
pupils.remove(94) # удалить по значению
print(pupils)
pupils.remove("Карим")
print(pupils)
print(pupils.pop(4)) # удалить и вытащить
print(pupils)
pupils.append("Арсен")
print(pupils)
pupils.sort() # сортировку
print(pupils)

#tuple - кортежи
# bad_peoples = ("Коля", "Бахмуд")
bad_peoples = "Коля", "Бахмуд", "Арсен"
print(bad_peoples)
print(bad_peoples)

# set - множества. неупорядоченные и не повторяющиеся
numbers1 = {4, 5, 7, 9, 9} 
print(numbers1)
numbers2 = {6, 7, 8, 4}
print(numbers1 & numbers2) # пересечение 
print(numbers1 | numbers2) # объединение
print(numbers1 - numbers2) #  разность 

#  преобразование к множеству и пересечение
print(set(pupils) & set(bad_peoples))
