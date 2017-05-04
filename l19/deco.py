def do_nice(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return str(result) + "!!!"
    return wrapper

def hello(name):
    return "Привет " + name

@do_nice
def sum5(a,b):
    return a + b + 5

print(hello("Арсен"))
print(do_nice(hello)("Арсен"))
# nice5 = do_nice(sum5)
# print(nice5(5,6))

print(sum5(5,5))