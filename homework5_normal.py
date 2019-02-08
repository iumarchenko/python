from homework5_easy import make_dir, del_dir, get_folder
import sys
import os
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
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

def process_user_choice(choice):
    if choice == 1:
        dir = input(color.Magenta + "Укажите директорию для перехода: " + color.END)
        if os.path.exists(dir):
            try:
                os.chdir(dir)
            except OSError:
                print("При переходе в директорию произошла ошибка")
        else:
            print("Директория " + dir + " не существует")
    elif choice == 2:
        print(color.Magenta + "Текущая директория " + os.getcwd() + " содержит следующие файлы и папки:" + color.END)
        list(map(print, get_folder()))
    elif choice == 3:
        dir = input(color.Magenta + "Укажите директорию для удаления: " + color.END)
        del_dir(dir)
    elif choice == 4:
        dir = input(color.Magenta + "Укажите директорию для создания:" + color.END)
        make_dir(dir)
    else:
        print(color.Red + "Выбрано неверное значение, попробуйте еще раз" + color.END)


while True:
    choice = input(color.Magenta + 'Выберите пункт:\n'
                   '    1. Перейти в папку\n'
                   '    2. Просмотреть содержимое текущей папки\n'
                   '    3. Удалить папку\n'
                   '    4. Создать папку\n'
                   '    5. Выход\n'
                   '---------------------\n'
                   'Ваш выбор: ' + color.END).strip()
    try:
        choice = int(choice)
    except ValueError:
        print(color.Red + "Выбрано неверное значение, попробуйте еще раз" + color.END)
        continue
    if choice == 5:
        break
    process_user_choice(choice)