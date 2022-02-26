import csv


def writeInCSV(goodsDictLocal):
    try:
        with open("file.csv", "w", newline='') as file:
            w = csv.writer(file)
            w.writerows(goodsDictLocal.items())
    except Exception as exc:
        print(exc)


def userInput():
    userCommand = input()
    return userCommand


def showGoods():
    try:
        with open("file.csv", "r") as file:
            r = csv.reader(file)
            dictGoods = dict(r)
            for key, value in dictGoods.items():
                print(key)
                valueDict = eval(value)
                for key2, value2 in valueDict.items():
                    print(key2, '->', value2)
                print()
    except Exception as exc:
        print(exc)


def userInputAdd(goodsDictLocal):
    userAddName = input('Введите название товара\n')
    while True:
        try:
            userAddPrice = int(input('Введите цену\n'))
            if userAddPrice < 0:
                print('Число меньше нуля')
                continue
            else:
                break
        except:
            print('Вы ввели не число')
    userAdddescription = input('Введите описание товара\n')
    addDict = {
        userAddName : {
            "price" : str(userAddPrice),
            "description" : userAdddescription
        }
    }
    if userAddName not in (goodsDictLocal.keys()):
        try:
            with open("file.csv", "a", newline='') as file:
                w = csv.writer(file)
                w.writerows(addDict.items())
            goodsDictLocal.update(addDict)
        except:
            print(Exception)
    else:
        print('Такой товар уже существует')


def userInputDel(goodsDictLocal):
    userAddName = input('Введите название товара\n')
    if userAddName in goodsDictLocal.keys():
        goodsDictLocal.pop(userAddName)
    else:
        print('Такого товара нет')
        return
    try:
        with open("file.csv", "w", newline='') as file:
            w = csv.writer(file)
            w.writerows(goodsDictLocal.items())
    except Exception as exc:
        print(exc)


def userInputSearch(goodsDictLocal):
    userSearchName = input('Введите название товара\n')
    if userSearchName in goodsDictLocal.keys():
        searchDict = {
            userSearchName: {
                "price": goodsDictLocal[userSearchName]['price'],
                "description": goodsDictLocal[userSearchName]['description']
            }
        }
        for key, value in searchDict.items():
            print(key)
            for key2, value2 in value.items():
                print(key2, '->', value2)
            print()
    else:
        print('Такого товара нет')
        return


goodsDict = {
    "goods1" : {
        "price" : "1000",
        "description" : "description of goods1"
    },
    "goods2" : {
        "price" : "500",
        "description" : "description of goods2"
    },
    "goods3" : {
        "price" : "3000",
        "description" : "description of goods3"
    }
}


writeInCSV(goodsDict)
while True:
    print("list - отображение всех существующих товаров")
    print("add - добавление товара")
    print("delete - удаление товара")
    print("search - поиск товара")
    print("q - выход")
    command = userInput()
    if command.lower() == 'list':
        showGoods()
    elif command.lower() == 'add':
        userInputAdd(goodsDict)
    elif command.lower() == 'delete':
        userInputDel(goodsDict)
    elif command.lower() == 'search':
        userInputSearch(goodsDict)
    elif command.lower() == 'q':
        break
    else:
        print('Такой команды не существует')
