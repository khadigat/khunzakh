class Weapon:
    def __init__(self,name,damage,count):
        self.name = name
        self.damage = damage
        self.count = count


class Character:
    def __init__(self,name,hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, victim):
        victim.hp -= self.damage
        print("{0.name} нанес {1.name} {0.damage} урона".format(
            self,victim))

class Zombie(Character):
    pass

class Player(Character):
    def __init__(self,name,hp, damage, weapon):
        super().__init__(name,hp, damage)
        self.weapon = weapon

    def attack(self, victim):
        damage = self.damage + self.weapon.damage
        victim.hp -= damage
        print("{0.name} нанес {1.name} {2} урона".format(
            self,victim,damage))

class Game:
    def start(self):
        weapon = Weapon("Томар", 100, 3)
        player = Player("Омар",1000, 5, weapon)
        zombie = Zombie("Арсн",300, 50)
        count = 0
        while True:
            player.attack(zombie)
            zombie.attack(player)
            print("Жизни игрока:",player.hp)
            print("Жизни зомби:",zombie.hp)
            input()
            if player.hp <= 0:
                print(player.name,"умер но убил ",count,"зомби")
                break
            if zombie.hp <= 0:
                count += 1
                zombie = Zombie("Арсн",300, 50)
                print(player.name,"убил зомби")

game = Game()
game.start()