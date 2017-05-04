import random

def create_player():
    player = {}
    player["Имя"] = input("Введите имя игрока: ")
    player["Жизни"] = 1000
    player["Атака"] = 64
    boost = input("Увеличить жизни - 1. Увеличить атаку - 2: ")
    if boost == "1":
        player["Жизни"] += 200
    else:
        player["Атака"] += 20
    return player

def hit(agressor, victim):
    damage = agressor["Атака"] + random.randint(
        -agressor["Атака"],agressor["Атака"])
    victim["Жизни"] -= damage
    
    if damage == 0:
        print("Промазал")
    if damage == agressor["Атака"] * 2:
        print("Крит!!!")

    print("{0[Имя]} нанес {1[Имя]} {2} урона".format(
        agressor,victim,damage))

def show_params(player):
    print("{0[Имя]}: {0[Жизни]}".format(player))

def fight(player1, player2):
    while True:
        hit(player1, player2)
        hit(player2, player1)
        show_params(player1)
        show_params(player2)
        input()
        if player1["Жизни"] <= 0:
            print(player2["Имя"],"убил", player1["Имя"])
            break
        if player2["Жизни"] <= 0:
            print(player1["Имя"],"убил", player2["Имя"])
            break


player1 = create_player()
player2 = create_player()
# print(player1, player2)
fight(player1, player2)