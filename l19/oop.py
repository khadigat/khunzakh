class Pen:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.ink = 10

    def write(self):
        if self.ink > 0:
            self.ink -= 2 
            print("ручка пишет")
        else:
            print("Кончились чернила")

class Car:
    def __init__(self,model,color,fuel, speed):
        self.model = model
        self.color = color
        self.fuel = fuel
        self.speed = speed

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 10
            print(self.model, "проехала", self.speed ,"километров")
        else:
            print("Кончилось топливо")

class GasStation:
    def fill_up(self,car,fuel):
        car.fuel += fuel



gel_pen = Pen('Красный',12)
print(gel_pen.color)
gel_pen.size -= 2
print(gel_pen.size)
gel_pen.write()
gel_pen.write()
print("-"*10)
simple_pen = Pen('Синяя',6)
simple_pen.write()
simple_pen.write()
simple_pen.write()
simple_pen.write()
simple_pen.write()
simple_pen.write()
simple_pen.write()

gel_pen.write()
gel_pen.write()
gel_pen.write()
gel_pen.write()

lada_vesta = Car("Лада веста","Желтый",20,60) 
nisan = Car("Нисан","Белый",30,100)
lada_vesta.drive()
lada_vesta.drive()
lada_vesta.drive()
nisan.drive()
nisan.drive()
nisan.drive()
nisan.drive()

sss_station = GasStation()
sss_station.fill_up(nisan,10)
nisan.drive()
nisan.drive()