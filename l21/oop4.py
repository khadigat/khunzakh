class Equipment:
    def __init__(self, model, cost):
        self.model = model
        self.cost = cost
  
    def run(self):
        print("Техника работает")

class Computer(Equipment):
    def run(self):
        print("Запускаю вам игру")

class Phone(Equipment):
    def __init__(self, model, cost):
        super().__init__(model,cost)
        self.__wifi = False

    def run(self, target):
        print("Соединяю вас с", target)

    def on_wifi(self):
        print("подключаемся к вайфаю")
        self.__wifi = True

    @property
    def wifi(self):
        return self.__wifi

    @wifi.setter
    def wifi(self, value):
        self.__wifi = value
        print("Не меняй вай фай")

    def __str__(self):
        return self.model



macbook = Computer("Mac Book pro", 10000000)
meizu = Phone("Meizu m3 mini", 8800)

macbook.run()
meizu.run("Арсеном")
# print(meizu.wifi)
meizu.on_wifi()
print(meizu.wifi)
print(meizu)
# meizu.__wifi = False
print(meizu.wifi)
meizu.wifi = True