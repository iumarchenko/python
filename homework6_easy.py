import sys
import os

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed=0, color = "white",name = "smth Car", is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина " + self.name + " поехала")

    def stop(self):
        print("Машина " + self.name + " остановилась")

    def turn(self, direction):
        print("Машина " + self.name + " повернула " + direction)

    def __str__(self):
        return "speed: {}, color: {}, name: {}, is_police: {}".format(self.speed, self.color, self.name, self.is_police)

class TownCar(Car):
    def __init__(self, speed=0, color = "white",name = "smth Car"):
        super().__init__(speed, color, name, False)


class SportCar(Car):
    def __init__(self, speed=0, color = "white",name = "smth Car"):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed=0, color = "white",name = "smth Car"):
        super().__init__(speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed=0, color = "white",name = "smth Car"):
        super().__init__(speed, color, name, True)


a = TownCar()
b = SportCar(100, "black", "Mazda")
print(a)
print(b)