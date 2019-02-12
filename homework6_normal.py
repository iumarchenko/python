# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name="", health = 100, damage = 50, armor = 0.7):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self, who_attack, who_defend, damage):
        who_defend.health -= damage
        print('{} нанес {} урона {}, у того осталось {} жизней.'.format(who_attack.name, who_defend.name, damage, who_defend.health))

    def calculate_damage(self, damage, armor):
        return damage // armor

    def __str__(self):
        return "name: {}, health: {}, damage: {}, armor: {}".format(self.name, self.health, self.damage, self.armor)

class Player(Person):
    def __init__(self, health = 100, damage = 50, armor = 0.7):
        name = input('Введите имя: ')
        super().__init__(name, health, damage, armor)

    def attack(self, enemy):
        damage = self.__calculate_damage(enemy.armor)
        super().attack(self, enemy,damage)

    def __calculate_damage(self, armor):
        return super().calculate_damage(self.damage, armor)


class Enemy(Person):
    def __init__(self, name="", health = 100, damage = 50, armor = 0.7):
        name = input('Введите имя: ')
        super().__init__(name, health, damage, armor)

    def attack(self, player):
        damage = self.__calculate_damage(player.armor)
        super().attack(self,player,damage)

    def __calculate_damage(self, armor):
        return super().calculate_damage(self.damage, armor)

class Game():
    def start_game(player, enemy):
        # Запоминаем кто последний атаковал
        last_attacker = player
        while player.health > 0 and enemy.health > 0:
            if last_attacker == player:
                enemy.attack(player)
                last_attacker = enemy
            else:
                player.attack(enemy)
                last_attacker = player
        if player.health > 0:
            print('Игрок победил!')
        else:
            print('Враг победил!')


player = Player(120, 70, 0.8)
enemy = Enemy()
Game.start_game(player, enemy)
