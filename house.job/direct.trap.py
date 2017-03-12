import math
AB = int(input("Длина первого катета: "))
AC = int(input("Длина гипотенузы: "))
BC = (math.sqrt(AC * AC - AB * AB)) 
print("Длина второго катета: ", BC)