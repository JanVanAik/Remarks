# remark = [{"id": 1, "name": "main", "body": "dobby", "datetimeCreation": "datetime",
#            "dateTimeEdit": "Datetime"}]
import datetime
import json

Storage = []

def create(name, body):
    date = datetime.datetime.now()
    Storage.append({"id": len(Storage) if len(Storage) > 0 else 1,
                 "name": name.ltrim(),
                 "body": body,
                 "dtCreation": date,
                 "dtLastEdit": datetime.datetime.now()})
    return f'Заметка с названием {name} создана'


def choice(name):
    counter = 0
    choiceList = []
    for i in Storage:
        if i[name] == name:
            choiceList.append((i))
    if counter == 0:
        return None
    elif counter == 1:
        return(choiceList[0])
    else:
        idDel = input(f'Заметок с таким именем несколько, вот они{choiceList}.'
                      f' Пожалуйста, введите id нужной заметки')
        for i in choiceList:
            if i[id] == idDel:
                return i


def delete(name):
    res = choice(name)
    if res == None:
        return 'Такой заметки нет'
    else:
        Storage.remove(res)
        return 'Заметка удалена'


def edit(name):
    pass




# def delete(name):
#     counter = 0
#     delList = []
#     for i in Storage:
#         if i[name] == name:
#             delList.append((i))
#     if counter == 0:
#         return 'Такой заметки нет'
#     elif counter == 1:
#         Storage.remove(delList[0])
#         return "Заметка удалена"
#     else:
#         idDel = input(f'Заметок с таким именем несколько, вот они{delList}.'
#                       f' Пожалуйста, введите id заметки, которую хотите удалить')
#         for i in delList:
#             if i[id] == idDel:
#                 Storage.remove(i)
#                 return 'Заметка удалена'


def read(name):
    for i in Storage:
        if i[name] == name:
            return i


def amount():
    return f'Всего у вас {len(Storage)} заметок '


while True:
    UserChoice = input("Введите требуемое действие:  "
                       "'create' - создать заметку, "
                       "'edit' - редактировать заметку, "
                       "'delete' - удалить заметку, "
                       "'read' - получить информацию о заметке, "
                       "'amount' - узнать общее количество заметок"
                       "'parse' - перевести заметки в json формат для передачи данных "
                       "'exit' - закончить работу программы\n")

    # Создание замети
    if UserChoice == "create":
        print(create(input('Введите название заметки:\n'), input('Введите текст заметки:\n')))

    # Редактирование заметок
    elif UserChoice == "edit":
        pass

    #  Удаление заметок
    elif UserChoice == "delete":
        print(delete("Введите имя заметки, которую хотите удалить: "))

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
