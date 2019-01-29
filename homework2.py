import random
__autor__ = 'Марченко Инесса'
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

list_1 = [random.randint(-5,16) for i in range (16)]
list_2 = []
for i in list_1:
    if i >= 0 and i ** 0.5 == int(i ** 0.5):
        list_2.append(int(pow(i, 0.5)))

print ("Задача №1")
print ("Исходный список: ", list_1)
print ("Полученный список: ", list_2)




# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
day = ['первое', 'второе', 'третье', 'четвёртое', 'пятое', 'шестое', 'седьмое', 'восьмое',
       'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',  'тринадцатое', 'четырнадцатое', 'пятнадцатое',
       'шестнадцатое','семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
       'двадцать первое', 'двадцать второе', 'двадцать третье', 'двадацать четвёртое',
        'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
        'тридцатое', 'тридцать первое']
month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
print ("Задача №2")
date = input("Введите дату в формате dd.mm.yyyy: ").split(".")
if( len(date) == 3 and
    int(date[0]) <=31 and int(date[0]) > 0 and
    int(date[1]) <= 12 and int(date[1]) > 0):
    print("{0} {1} {2} года".format(day[int(date[0])-1], month[int(date[1])-1], int(date[2])))
else:
    print("Введена дата в некорректном формате")



# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
print ("Задача №3")
n = random.randint(10,20)
print("n = ", n)
print("Полученный список: ", [random.randint(-100,100) for i in range (n)])

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print ("Задача №4")
# исходный список
list_3 = [random.randint(0,10) for i in range (15)]
list_3.sort()

# новый список (НЕ МНОЖЕСТВО?..), элементами которого будут неповторяющиеся элементы исходного списка:
list_4 = list(set(list_3))

# новый список, элементами которого будут элементы исходного списка, которые не имеют повторений:
# var 1
list_5 = []

for i in range(10):
    if list_3.count(list_3[i]) == 1:
        list_5.append(list_3[i])


# var 2
list_6 = list_3.copy()
for i in list_6:
    if list_6.count(i) > 1:
        while list_6.count(i) > 0:
            list_6.remove(i)

print("Исходный список: ",list_3)
print("Преобразованный список 1 (неповторяющиеся элементы): ",list_4)
print("Преобразованный список 1 (элементы не имеют повторений): ",list_5)
print("Преобразованный список 1 (элементы не имеют повторений): ",list_6)