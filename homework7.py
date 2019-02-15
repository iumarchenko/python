import random
count = 1

class lotto_ticket():
    def __init__(self, name = ""):
        global count
        if len(name.strip()) > 0:
            self.name = name
        else:
            self.name = "Игрок " + str(count)
            count += 1
        self.loss = False
        self.__numbers = set()
        while len(self.__numbers) < 15:
            self.__numbers.add(random.randint(1, 90))
        self.__numbers = list(self.__numbers)
        self.__numbers[0:5] = sorted(self.__numbers[0:5])
        self.__numbers[5:10] = sorted(self.__numbers[5:10])
        self.__numbers[10:15] = sorted(self.__numbers[10:15])
        self.__spaces = [random.randint(1,6) for i in range(15)]
        self.__makeStr()

    def __makeStr(self):
        res = '------------------------------\n'
        for i in range(3):
            temp = [str(x) for x in self.__numbers[i*5:i*5+5]]
            for j in range(5):
                temp[j] = temp[j].rjust(self.__spaces[i+j])
            res += ' '.join(temp)
            res += '\n'
        res += '------------------------------'
        self.__numbers_str = res

    def isHave(self, a):
        return True if a in self.__numbers else False

    def isWin(self):
        return True if len(self.__numbers) == 0 else False

    def deleteNumber(self, a):
        if self.isHave(a):
            self.__numbers[self.__numbers.index(a)] = "-"
            self.__makeStr()

    def __str__(self):
        return 'Билет ' + self.name + ':\n' + self.__numbers_str

class game():
    def __init__(self):
        self.__player = lotto_ticket()
        self.__computer = lotto_ticket()
        self.__avail_numbers = set(i for i in range(1, 90))

    def start(self):
        for i in range(1, 90):
            cur_number = random.choice(list(self.__avail_numbers))
            self.__avail_numbers.remove(cur_number)
            print('\n\033[91mНовый бочонок: {}, осталось {} бочонков\033[0m'.format(str(cur_number), str(len(self.__avail_numbers))))
            print(self.__player)
            print(self.__computer)
            self.__playerMove(cur_number)
            if self.__isGameEnd():
                break
            self.__computerMove(cur_number)
            if self.__isGameEnd():
                break

    def __playerMove(self, cur_number):
        while True:
            step = input("\033[92mЗачеркнуть цифру? (y/n)\033[0m")
            if step == "y":
                print("Ход игрока: зачеркнута ячейка")
                if self.__player.isHave(cur_number):
                    self.__player.deleteNumber(cur_number) # все ок
                else:
                    self.__player.loss = True
                break
            elif step == "n":
                print("Ход игрока: продолжить")
                if self.__player.isHave(cur_number):
                    self.__player.loss = True # проигрыш
                break
            else:
                print("\033[92mВы ввели что-то не то, выберите еще раз\033[0m")

    def __computerMove(self, cur_number):
        if self.__computer.isHave(cur_number):
            self.__computer.deleteNumber(cur_number)
            print("Ход компьютера: зачеркнута ячейка")
        else:
            print("Ход компьютера: продолжить")

    def __isGameEnd(self):
        if self.__player.loss:
            print("{} проиграл... Игра закончена".format(self.__player.name))
            return True
        if self.__player.isWin():
            self.win(self.__player)
            print("Выиграл {} !!!!! Игра закончена".format(self.__player.name))
            return True
        if self.__computer.isWin():
            self.win()
            print("Выиграл {} !!!!! Игра закончена".format(self.__computer.name))
            return True
        if len(self.__avail_numbers) == 0:
            return True
        return False

game().start()
