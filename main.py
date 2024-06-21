#

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        return print(other.name, "осталось", other.health, "жизней")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Game:
    def __init__(self):
        self.player = Hero("Player")
        self.computer = Hero("Computer")

    def start(self):
        while True:
            print(self.player.name, "атакует")
            self.player.attack(self.computer)
            if self.computer.is_alive() == False:
                print(self.player.name, "победил!")
                break
            print(self.computer.name, "атакует")
            self.computer.attack(self.player)
            if self.player.is_alive() == False:
                print(self.computer.name, "победил!")
                break


g = Game()

g.start()








