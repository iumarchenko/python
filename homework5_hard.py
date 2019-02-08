# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name>")
    print("cd <full_path or relative_path>")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return


    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.makedirs(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))
    except Exception as ex:
        print('при создании директории {} произошла ошибка'.format(dir_name))
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)


def ping():
    print("pong")

def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return

    file_path = os.path.join(os.getcwd(), dir_name)
    filename = os.path.basename(file_path)
    if os.path.exists(file_path):
        new_filename = filename.split(".")[0] + '_copy.py'
        if os.name == "nt":
            if os.popen('copy ' + file_path + ' ' + new_filename):
                print ("Файл " + filename + " скопирован")
        else:
            if os.popen('cp ' + file_path + ' ' + new_filename):
                print("Файл " + filename + " скопирован")
    else:
        print("Файл " + filename + " не существует")

def delete_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return

    file_path = os.path.join(os.getcwd(), dir_name)
    filename = os.path.basename(file_path)
    if os.path.exists(file_path):
        try:
            os.remove (file_path, dir_fd=None)
            print("Файл " + filename + " успешно удален")
        except OSError:
            print("При удалении файла " + filename + " произошла ошибка")
    else:
        print("Файл " + filename + " не существует")

def change_dir():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return

    if os.path.exists(dir_name):
        try:
            os.chdir(dir_name)
            print("Текущая директория " + dir_name)
        except OSError:
            print("При переходе в директорию произошла ошибка")
    else:
        print("Директория " + dir_name + " не существует")

def current_path():
    print(os.getcwd())

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": delete_file,
    "cd": change_dir,
    "ls": current_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")