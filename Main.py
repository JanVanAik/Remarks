from datetime import datetime
import json

Storage = []
# Программа сохраняет заметки в имеющийся список и, при необходимости, парсит его в json
# Парсить заметку сразу, при создании, не оптимально. Наиболее оптимальный вариант - иметь txt файл,
# а его уже, при необходимости, убирать в json, но текущая реализация, на мой взгляд, тоже подходит.
# При этом, возможность закачки сразу в файл тоже реализовал и чтения из него
def create(name, body):
    date = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")

    Remark = {"id": len(Storage)+1 if len(Storage) > 0 else 1,
                 "name": name,
                 "body": body,
                 "dtCreation": date,
                 "dtLastEdit": date}
    Storage.append(Remark)

    # Реализация для немедленного парсинга заметки в файл
    # with open (f"{Remark['name']}.json", 'w') as file:
    #             json.dump(Storage, file)
    #             print("Ваш файл json готов. ")

    return f'Заметка с названием {name} создана'


# Функция для извлечения и конвертации json.str в python.dict.
def extractRemark(file):
    with open(file, "r") as file:
        dictFromJson = json.loads(file.read())
        return dictFromJson


def choice(name):
    counter = 0
    choiceList = []
    for i in Storage:
        if i['name'] == name:
            choiceList.append((i))
            counter +=1
    if counter == 0:
        return None
    elif counter == 1:
        return(choiceList[0]['id'])
    else:
        idChoice = input(f'Заметок с таким именем несколько, вот они\n{choiceList}\n.'
                      f' Пожалуйста, введите id нужной заметки: \n')
        for i in choiceList:
            if i['id'] == int(idChoice):
                return idChoice


def delete(name):
    res = choice(name)
    if res == None:
        return 'Такой заметки нет'
    else:
        for i in Storage:
            if i['id'] == res:
                Storage.remove(i)
                return 'Заметка удалена'


def edit(name):
    res = choice(name)
    if res == None:
        return 'Такой заметки нет'
    else:
        for i in Storage:
            if i["id"] == int(res):
                userReaction = input(f'Вот старый текст заметки\n*****\n{i["body"]}\n*****\n'
                                     f'Введите новый текст заметки: \n')
                i['body'] = userReaction
                return 'Заметка изменена'


def read(name):
    res = choice(name)
    if res == None:
        return 'Такой заметки нет'
    else:
        for i in Storage:
            if i['id'] == int(res):
                return i

def readAll():
    res = ''
    for i in Storage:
        res += f"{i}\n"
    return res


def amount():
    return f'Всего у вас {len(Storage)} заметок '


while True:
    UserChoice = input("Введите требуемое действие:\n"
                       "'create' - создать заметку\n"
                       "'edit' - редактировать заметку \n"
                       "'delete' - удалить заметку\n"
                       "'read' - получить информацию о заметке\n"
                       "'readall' - получить весь список заметок"
                       "'amount' - узнать общее количество заметок\n"
                       "'parse' - перевести заметки в json формат для передачи данных \n"
                       "'exit' - закончить работу программы\n")

    # Создание замети
    if UserChoice == "create":
        print(create(input('Введите название заметки:\n'), input('Введите текст заметки:\n')))

    # Редактирование заметок
    elif UserChoice == "edit":
        print(edit(input('Введите название заметки:\n')))

    #  Удаление заметок
    elif UserChoice == "delete":
        print(delete(input("Введите имя заметки, которую хотите удалить: ")))

    #  Чтение заметок
    elif UserChoice == "read":
        Res = read(input("Введите имя заметки:\n"))
        if Res == None:
            print("Такой заметки нет")
        else:
            print(Res)

    #  Чтение списка заметок
    elif UserChoice == "readall":
        print(readAll())

    # Узнать количество заметок
    elif UserChoice == "amount":
        print(amount())

    # Спарсить в json
    elif UserChoice == "parse":
        with open("remarks.json", 'w') as file:
            json.dump(Storage, file)
            print("Ваш файл remarks.json готов. ")

    # Выйти из программы
    elif UserChoice == "exit":
        break
