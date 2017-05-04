class Animal:
    def __init__(self, name, color, age, power):
        self.name = name
        self.color = color
        self.age = age
        self.power = power

    def say(self):
        print("Я животное")

    def run(self):
        print(self.name,"побежала за вами")

    def __add__(self, other):
        return self.age + other.age

    def __lt__(self, other):
        return self.power < other.power

    def __str__(self):
        return self.name

class Dog(Animal):
    def say(self):
        print("Гав гав")

    def bite(self,somebody):
        print("{0.name} укусила {1}".format(self,somebody))

class Cat(Animal):
    def __init__(self, name, color, age, power, claws):
        super().__init__(name, color, age, power)
        self.claws = claws

    def say(self):
        print("Мяу мяу")



alisa = Dog("Алиса","желтый", 3, 1000)
alisa.run()
alisa.say()
vasya = Cat("Вася","черный", 5, 10000,"острейшие")
vasya.say()
alisa.bite(vasya.name)
print(2 + 2)
print(alisa + vasya)
print(alisa > vasya)
print(alisa)