import random
# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

color = ["white", "black", "yellow", "blue", "red"]
type = ["animal", "cartoon"]

class Toy:
    def __init__(self, name="", color = random.choice(color), type_toy = random.choice(type)):
        self.name = name
        self.color = color
        self.type = type_toy

    def __str__(self):
        return "name: {}, color: {}, type: {}".format(self.name, self.color, self.type)


class Animal(Toy):
    def __init__(self, name="", color=random.choice(color)):
        super().__init__(name, color, type[0])

class Cartoon(Toy):
    def __init__(self, name="", color=random.choice(color)):
        super().__init__(name, color, type[1])

class Factory():
    def __init__(self):
        self.name = 'Фабрика игрушек'

    def __purchase(self, name):
        print("Выполняется закупка материалов для создания игрушки " + name)

    def __sewing(self, name):
        print("Выполняется пошив для создания игрушки " + name)

    def __coloring(self, name):
        print("Выполняется покраска для создания игрушки " + name)

    def CreateToy(self):
        name = input("Введите название игрушки: ")
        self.__purchase(name)
        self.__sewing(name)
        self.__coloring(name)
        type_toy = random.choice(type)
        return Animal(name) if type_toy == "animal" else Cartoon(name)

    def __str__(self):
        return "name: {}".format(self.name)

a = Factory()
print(a)
b = a.CreateToy()
print(b)



