import random
import re
#EASY
# Все задачи текущего блока решите с помощью генераторов списков!
# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


list_len = random.randint(5, 10)
list_1 = [random.randint(0, 10) for _ in range(list_len)]
list_2 = [list_1[_]**2 for _ in range(list_len)]
print(list_1)
print(list_2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
list_3 = ["apple", "nectarine", "apricot", "pear", "banana", "grapes", "mango"]
list_4 = ["nectarine", "orange", "pear", "banana", "pineapple", "peach", "grapes", "mango"]
list_5 = [list_3[_] for _ in range(len(list_3)) if list_3[_] in list_4]
print(list_5)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
list_len = random.randint(10, 20)
list_6 = [random.randint(-5, 15) for _ in range(list_len)]
list_7 = [list_6[_] for _ in range(list_len) if list_6[_] > 0 and list_6[_] % 3 == 0 and list_6[_] % 4 != 0]
print(list_6)
print(list_7)


#MEDIUM
# Эти задачи необходимо решить используя регулярные выражения!
# Задача - 1
# Запросите у пользователя имя, фамилию, email.
# Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате:
# текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст,
# допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.
pat_name = "^[А-Я]{1}[а-я]{2,20}$"
pat_fam = "^[А-Я]{1}[а-я]{2,20}$"
pat_email = "^[a-z_0-9]+@{1}[a-z0-9]*\.(ru|org|com)$"

name, family, email = input("Введите пожалуйста имя: "), input("Введите пожалуйста фамилию: "), input("Введите пожалуйста e-mail: ")
print('Имя введено некорректно') if re.match(pat_name, name) is None else print('Имя введено корректно')
print('Фамилия введена некорректно') if re.match(pat_fam, family) is None else print('Фамилия введена корректно')
print('e-mail введен некорректно') if re.match(pat_email, email) is None else print('e-mail введено корректно')


# Задача - 2:
# Вам дан текст: .....
# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!
some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''
pat_str = "\.{2,}"
print('В тексте отсутствуют символы более одной точки подряд') if re.search (pat_str, some_str) is None else print('В тексте присутствуют символы более одной точки подряд')

# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

class color:
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Magenta = '\033[95m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Grey = '\033[90m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - float(money) >= 0:
        person['money'] -= money
        return color.Blue + 'Вы сняли {} рублей. Остаток по счету {} рублей'.format(money, person['money']) + color.END
    else:
        return color.Red + 'На вашем счету недостаточно средств!' + color.END

def check_count():
    while True:
        count = input(color.UNDERLINE + 'Сумма к снятию (руб. и коп. через "."):\n' + color.END).strip()
        if re.match('^\d+(\.\d{1,2})?$', count) is None or not re.match('^0+?$', count) is None:
            new_choice = input(color.Red + 'Сумма введена некорректно. Попробовать еще раз? (y/n):\n' + color.END).strip()
            if not re.match('^(y|n){1}$', new_choice) is None:
                if new_choice == 'y':
                    continue
                elif new_choice == 'n':
                    print(color.UNDERLINE + 'Выберите другую операцию'+color.END)
                    return False
            else:
                print(color.Red + "Вы не выбрали ни один из пунктов. Начните заново" + color.END)
                return False
        else:
            try:
                count = float(count)
                return count
            except Exception:
                print(color.Red + 'Произошла ошибка. Попробуйте выполнить операцию позже' + color.END)
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)



def process_user_choice(choice, person):
    if choice == '1':
        print(color.Blue + "Ваш баланс составляет: {} рублей".format(check_account(person)) + color.END)
    elif choice == '2':
        count = check_count()
        if count:
            print(withdraw_money(person, count))
    else:
        print(color.Red + "Выбран отсутствующий пункт" + color.END)


def start():
    for i in range(3):
        user_data = input(color.UNDERLINE + 'Введите номер карты и пин код через пробел:\n' + color.END).strip()
        if re.match("^[0-9]{16}\s{1}[0-9]{4}$", user_data) is None:
            if i < 2:
                print(color.Red + 'Вы ввели некорректные данные, попробуйте еще раз' + color.END)
            else:
                print(color.Red + 'Вы Исчерпали попытки, карта заблокирована, пожалуйста обратитесь в отделение банка' + color.END)
                return False
        else:
            card_number, pin_code = user_data.split()
            break
    try:
        card_number = int(card_number)
        pin_code = int(pin_code)
    except Exception:
         print(color.Red + 'Произошла ошибка. Попробуйте выполнить операцию позже' + color.END)
         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
         message = template.format(type(ex).__name__, ex.args)
         print(message)

    person = get_person_by_card(card_number)
    if person and is_pin_valid(person, pin_code):
        while True:
            choice = input(color.UNDERLINE + 'Выберите пункт:\n'  + color.END +
                               '    1. Проверить баланс\n'
                               '    2. Снять деньги\n'
                               '    3. Выход\n' 
                               '---------------------\n'
                               'Ваш выбор: ').strip()
            if not re.match("^[0-9]{1}$", choice) is None:
                if choice == '3':
                    break
                else:
                    process_user_choice(choice, person)
            else:
                print(color.Red + "Выбран отсутствующий пункт" + color.END)
    else:
        print(color.Red + 'Номер карты или пин код введены не верно!' + color.END)


start()