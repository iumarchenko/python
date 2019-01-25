msg = {
    "ok": "Все отлично, хорошее состояние",
    "fault_medical" : "Возможны проблемы со здоровьем, необходим врачебный осмотр",
    "fault_lifestyle" : "Вам необходимо начать вести здоровый образ жизни"}

people = {"name": "", "age": "", "weight" : ""}

# вывести сообщение о пациенте
def print_pacient(x, y):
    print('{0}, возраст (полных лет) {1}, вес {2} кг: {3}'.format(x["name"], x["age"], x["weight"], y))

# имя введено корректно и содержит только буквы и пробелы между словами
def only_letters(str):
    return all(letter.isalpha() for letter in str.split()) if len(str.split()) > 0 else False

# пока не будет нажат 0
while True:
    # на всякий случай чистим переменную
    for i in people.keys():
        people[i] = ""
    # ввод имени
    while not people["name"]:
        people["name"] = input ("Введите, пожалуйста, имя пациента: ")
        # если имя не пустое
        if len(people["name"]) > 0:
            # если введены буквы и пробелы
            if only_letters(people["name"]):
                # убираем лишние пробелы между словами и каждое слово будет начинаться с большой буквы
                people["name"] = ' '.join(people["name"].split())
                people["name"] = people["name"].title()
                break;
            else:
                print("Похоже вы ошиблись при вводе. Имя должно содержать только буквы. Попробуйте еще раз.")
                people["name"] = ""
        else:
            print("Вы ничего не ввели. Попробуйте еще раз.")

    # ввод возраста
    while not people["age"]:
        people["age"] = input("Введите, пожалуйста, возраст пациента в годах: ").strip()
        # если не пустое
        if len(people["age"]) > 0:
            # если состоит только из цифр, да, без точек, запятых и минусов
            if people["age"].isdigit():
                # в принципе и так из цифр, я не стала делать try...except... что может случиться...
                people["age"] = int(people["age"])
                # проверяем что возраст корректен, не 0 и не слишком большой
                if people["age"] <= 0 or people["age"] > 100:
                    print("Похоже вы ошиблись при вводе. Возраст человека не может быть нулевым или более 100 лет. Попробуйте еще раз.")
                    people["age"] = ""
            else:
                print("Похоже вы ошиблись при вводе. Возраст необходимо вводить цифрами. Попробуйте еще раз.")
                people["age"] = ""
        else:
            print("Вы ничего не ввели. Попробуйте еще раз.")

    # ввод веса
    while not people["weight"]:
        people["weight"] = input("Введите, пожалуйста, вес пациента в килограммах: ").strip()
        # если не пустое
        if len(people["weight"]) > 0:
            # если состоит только из цифр, да, без точек, запятых и минусов
            if people["weight"].isdigit():
                people["weight"] = int(people["weight"])
                # проверяем что вес корректен, не 0 и не слишком большой
                if people["weight"] <= 0 or people["weight"] > 300:
                    print("Похоже вы ошиблись при вводе. Вес человека не может быть нулевым или более 200кг. Попробуйте еще раз.")
                    people["weight"] = ""
            else:
                print("Похоже вы ошиблись при вводе. Вес необходимо вводить цифрами. Попробуйте еще раз.")
                people["weight"] = ""
        else:
            print("Вы ничего не ввели. Попробуйте еще раз.")

    # проверка условий
    if people["age"] < 30:
        if people["weight"] < 50:
            print_pacient(people, msg["fault_medical"])
        elif people["weight"] >= 50 and people["weight"] < 120:
            print_pacient(people, msg["ok"])
        else:
            print_pacient(people, msg["fault_medical"])
    elif people["age"] >= 30 and people["age"] < 40:
        if people["weight"] < 50:
            print_pacient(people, msg["fault_lifestyle"])
        elif people["weight"] >= 50 and people["weight"] < 120:
            print_pacient(people, msg["ok"])
        else:
            print_pacient(people, msg["fault_lifestyle"])
    else:
        if people["weight"] < 50:
            print_pacient(people, msg["fault_medical"])
        elif people["weight"] >= 50 and people["weight"] < 120:
            print_pacient(people, msg["fault_lifestyle"])
        else:
            print_pacient(people, msg["fault_medical"])
    ext = input("Для выхода нажмите 0. Если хотите продолжить нажмите любую другую клавишу: ").strip()
    if ext == "0":
        break;

