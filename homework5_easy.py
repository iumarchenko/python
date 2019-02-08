import sys
import os

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def make_dir(filename):
    if not os.path.exists(filename):
        try:
            os.mkdir(filename, mode=0o777)
            print("Директория " + filename + " успешно создана")
        except OSError:
            print("При создании директории произошла ошибка")
    else:
        print("Директория " + filename + " уже существует")

def del_dir(filename):
    if os.path.exists(filename):
        try:
            os.rmdir (filename, dir_fd=None)
            print("Директория " + filename + " успешно удалена")
        except OSError:
            print("При удалении директории " + filename + " произошла ошибка")
    else:
        print("Директория " + filename + " не существует")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def get_folder():
    return os.listdir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file(filename):
    filename = os.path.basename(filename)
    if os.path.exists(filename):
        new_filename = filename.split(".")[0] + '_copy.py'
        # if os.system('copy ' + filename + ' ' + filename+ '_copy.py') == 0:
        if os.name == "nt":
            if os.popen('copy ' + filename + ' ' + new_filename):
                print ("Файл " + filename + " скопирован")
        else:
            if os.popen('cp ' + filename + ' ' + new_filename):
                print("Файл " + filename + " скопирован")
    else:
        print("Файл " + filename + " не существует")

if __name__ == '__main__':
    for i in range(9):
        make_dir("dir_"+str(i+1))

    for i in range(9):
        del_dir("dir_"+str(i+1))

    copy_file(sys.argv[0])

    list_dir = [i for i in get_folder() if os.path.isdir(i)]
    print("Текущая директория " + os.getcwd() + " содержит следующие папки:")
    list(map(print, list_dir))

