# текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу,
# пока у одного из героев не закончится здоровье.
# # Требования:
# # Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# # Игра должна быть реализована как консольное приложение.

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power
        return other.health

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
        self.player.attack()





