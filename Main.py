# remark = [{"id": 1, "name": "main", "body": "dobby", "datetimeCreation": "datetime",
#            "dateTimeEdit": "Datetime"}]
import datetime
import json

Storage = []

def create(name, body):
    date = datetime.datetime.now()
    Storage.append({"id": len(Storage)+1 if len(Storage) > 0 else 1,
                 "name": name,
                 "body": body,
                 "dtCreation": date,
                 "dtLastEdit": datetime.datetime.now()})
    return f'Заметка с названием {name} создана'


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
            if i["id"] == res:
                userReaction = input(f'Вот старый текст заметки\n*****\n{i["body"]}\n*****\n'
                                     f'Введите новый текст заметки: \n')
                i['body'] = userReaction
                return 'Заметка изменена'




def read(name):
    for i in Storage:
        if i['name'] == name:
            return i


def amount():
    return f'Всего у вас {len(Storage)} заметок '


while True:
    UserChoice = input("Введите требуемое действие:\n"
                       "'create' - создать заметку\n"
                       "'edit' - редактировать заметку \n"
                       "'delete' - удалить заметку\n"
                       "'read' - получить информацию о заметке\n"
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
