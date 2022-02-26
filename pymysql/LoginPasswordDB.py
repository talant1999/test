import re
import pymysql.cursors


def createConnection():
    connect = pymysql.connect(host='localhost',
                              user='root',
                              password='',
                              db='HW7',
                              cursorclass=pymysql.cursors.DictCursor)
    return connect


def userInput():
    userCommand = input()
    return userCommand


def showUsers(connect):
    try:
        with connect.cursor() as cursor:
            cursor.execute("Select * from users")
            rows = cursor.fetchall()
            for row in rows:
                print(row['login'])
    except Exception as exc:
        print(exc)


def checkUserLogin(connect, userEnterLogin):
    try:
        with connect.cursor() as cursor:
            cursor.execute("Select * from users")
            rows = cursor.fetchall()
            for row in rows:
                if userEnterLogin == row["login"]:
                    return False
        return True
    except Exception as exc:
        print(exc)


def createUserPassword():
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


def userInputAdd(connect):
    print('Введите имя пользователя')
    userEnterLogin = userInput()
    if checkUserLogin(connect, userEnterLogin):
        userEnterPassword = createUserPassword()
        try:
            with connect.cursor() as cursor:
                sql = "insert into users (login, password) values (%s,%s)"
                val = (userEnterLogin, userEnterPassword)
                cursor.execute(sql, val)
                connect.commit()
        except Exception as exc:
            print(exc)
    else:
        print('Такой login уже существует')


def userChangePassword(connect):
    print('Введите имя пользователя')
    userEnterLogin = userInput()
    if not checkUserLogin(connect, userEnterLogin):
        userChangePassword = createUserPassword()
        try:
            with connect.cursor() as cursor:
                sql = "update users set login = %s, password = %s where login = %s"
                val = (userEnterLogin, userChangePassword, userEnterLogin)
                cursor.execute(sql, val)
                connect.commit()
        except Exception as exc:
            print(exc)
    else:
        print('Такой login не существует')


try:
    connection = createConnection()
    while True:
        print("1 - Вывести пользователей")
        print("2 - Добавить пользователя")
        print("3 - Изменить пароль")
        print("4 - Выход")
        command = userInput()
        if command.lower() == '1':
            showUsers(connection)
        elif command.lower() == '2':
            userInputAdd(connection)
        elif command.lower() == '3':
            userChangePassword(connection)
        elif command.lower() == '4':
            connection.close()
            break
        else:
            print('Такой команды не существует')
except Exception as exc:
    print(exc)
