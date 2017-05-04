while True:
    try:
        number = int(input("Введите число: "))
        print("5 / число:",5/number)
        break
    except ValueError:  
        print("Введите нормальное число")
        
    except ZeroDivisionError:
        print("Глупец, зачем ты делишь на ноль")
# raise ValueError

class AndreyError(Exception): 
    pass

name = input("Введите имя: ")
try:
    if name == "Андрей":
        raise AndreyError

except AndreyError:
    print("Откуда ты знаешь это имя??? ОШИБКА")