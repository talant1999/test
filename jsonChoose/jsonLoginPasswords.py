import json
import re


def writeInJSON(usersDictLocal):
    try:
        with open('loginsPasswords.json', 'w') as file:
            json.dump(usersDictLocal, file)
    except Exception as exc:
        print(exc)


def downloadUsersFromJSON(usersDictLocal):
    with open("loginsPasswords.json", "r") as file:
        usersDictLocal = json.load(file)
    return usersDictLocal


def userInput():
    userCommand = input()
    return userCommand


def showUsers(usersDictLocal):
    try:
        print('logins:')
        for i in usersDictLocal['users']:
            print(i['login'])
    except Exception as exc:
        print(exc)


def checkUserLogin(usersDictLocal, isNeedPassword):
    userAddLoginLocal = input('Введите login пользователя\n')
    i = 0
    isExistLocal = False
    while i != len(usersDictLocal['users']):
        try:
            if userAddLoginLocal == usersDictLocal['users'][i]['login']:
                isExistLocal = True
                if isNeedPassword:
                    userPassword = usersDictLocal['users'][i]['password']
                    return isExistLocal, userAddLoginLocal, userPassword, i
                else:
                    return isExistLocal, userAddLoginLocal
            else:
                i += 1
                continue
        except Exception as exc:
            print(exc)
            break
    if isNeedPassword:
        userPassword = ''
        i = 0
        return isExistLocal, userAddLoginLocal, userPassword, i
    else:
        return isExistLocal, userAddLoginLocal


def checkUserPassword():
    while True:
        try:
            print('Пароль должен содержать не менее 8 символов')
            print('Пароль должен включать буквы верхнего регистра')
            print('Пароль должен включать буквы нижнего регистра')
            print('Пароль должен включать цифры')
            print('Пароль должен включать специальные символы: !, $, %, &')
            userAddPassword = input('Введите пароль\n')
            levelPassword = 0
            rool = []
            rool.append('^.{8,}$')
            rool.append('^.*[A-Z]+.*$')
            rool.append('^.*[a-z]+.*$')
            rool.append('^.*[0-9]+.*$')
            rool.append('^.*[\W]+.*$')
            for i in rool:
                if re.fullmatch(i, userAddPassword):
                    levelPassword += 1
                else:
                    continue
            if levelPassword <= 2:
                print('Пароль слишком слабый')
                continue
            elif levelPassword <= 4:
                userChoice = input('Ваш пароль может быть сильнее. Для ввода пароля заново введите (y). Для сохранения текущего пароля введите любой символ\n')
                if userChoice == 'y':
                    continue
                else:
                    print('Ваш пароль сохранен')
                    break
            else:
                print('Ваш пароль сильный, он сохранен')
                break
        except Exception as exc:
            print(exc)
    return userAddPassword


def userInputAdd(usersDictLocal):
    while True:
        try:
            isExistUser, userAddLogin = checkUserLogin(usersDictLocal, noNeedPassword)
            if isExistUser:
                print('Такой login уже существует')
                continue
            userAddPassword = checkUserPassword()
            if not isExistUser:
                break
        except Exception as exc:
            print(exc)
            return
    addDict = {
        "login": userAddLogin,
        "password": userAddPassword
    }
    usersDictLocal['users'].append(addDict)
    writeInJSON(usersDictLocal)


def userChangePassword(usersDictLocal):
    isExistUser, userLoginToChangePassword, userPassword, item = checkUserLogin(usersDictLocal, needPassword)
    if isExistUser:
        userChangePassword = checkUserPassword()
        if userChangePassword == userPassword:
            print('Вы ввели старый пароль')
        else:
            usersDictLocal['users'][item]['password'] = userChangePassword
            writeInJSON(usersDictLocal)
    else:
        print('Такой login не существует')


usersDict = {}
needPassword = True
noNeedPassword = False
try:
    usersDict = downloadUsersFromJSON(usersDict)
    #print(usersDict)
    while True:
        print("1 - Вывести пользователей")
        print("2 - Добавить пользователя")
        print("3 - Изменить пароль")
        print("4 - Выход")
        command = userInput()
        if command.lower() == '1':
            showUsers(usersDict)
        elif command.lower() == '2':
            userInputAdd(usersDict)
        elif command.lower() == '3':
            userChangePassword(usersDict)
        elif command.lower() == '4':
            break
        else:
            print('Такой команды не существует')
except Exception as exc:
    print(exc)
