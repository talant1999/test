def userNum():
    while True:
        print('Введите одну цифру')
        myNum = input()
        if myNum.lower() == "stop":
            global isStop
            isStop = True
            break
        else:
            try:
                num = int(myNum)
                if len(myNum) != 1:
                    print('Вы ввели число')
                    continue
                else:
                    return num
            except Exception:
                print('Вы ввели не цифру')
                continue


questionsDict = {
    "quest1" : {
        "question": "Вопрос 1",
        "answers" : {
        "1":"Ответ 1",
        "2":"Ответ 2",
        "3":"Ответ 3",
        "4":"Ответ 4"
        },
        "result" : "2"
    },
    "quest2" : {
        "question": "Вопрос 2",
        "answers" : {
        "1":"Ответ 1",
        "2":"Ответ 2",
        "3":"Ответ 3",
        "4":"Ответ 4"
        },
        "result" : "4"
    },
    "quest3" : {
        "question": "Вопрос 3",
        "answers" : {
        "1":"Ответ 1",
        "2":"Ответ 2",
        "3":"Ответ 3",
        "4":"Ответ 4"
        },
        "result" : "3"
    },
    "quest4" : {
        "question": "Вопрос 4",
        "answers" : {
        "1":"Ответ 1",
        "2":"Ответ 2",
        "3":"Ответ 3",
        "4":"Ответ 4"
        },
        "result" : "1"
    },
    "quest5" : {
        "question": "Вопрос 5",
        "answers" : {
        "1":"Ответ 1",
        "2":"Ответ 2",
        "3":"Ответ 3",
        "4":"Ответ 4"
        },
        "result" : "3"
    },
    "quest6" : {
        "question": "Вопрос 6",
        "answers" : {
        "1":"Ответ 1",
        "2":"Ответ 2",
        "3":"Ответ 3",
        "4":"Ответ 4"
        },
        "result" : "3"
    },
    "quest7" : {
        "question": "Вопрос 7",
        "answers" : {
        "1":"Ответ 1",
        "2":"Ответ 2",
        "3":"Ответ 3",
        "4":"Ответ 4"
        },
        "result" : "1"
    },
    "quest8" : {
        "question": "Вопрос 8",
        "answers" : {
        "1":"Ответ 1",
        "2":"Ответ 2",
        "3":"Ответ 3",
        "4":"Ответ 4"
        },
        "result" : "2"
    },
    "quest9" : {
        "question": "Вопрос 9",
        "answers" : {
        "1":"Ответ 1",
        "2":"Ответ 2",
        "3":"Ответ 3",
        "4":"Ответ 4"
        },
        "result" : "4"
    },
    "quest10" : {
        "question": "Вопрос 10",
        "answers" : {
        "1":"Ответ 1",
        "2":"Ответ 2",
        "3":"Ответ 3",
        "4":"Ответ 4"
        },
        "result" : "4"
    }
}

resultAnswer = ''
sum = 0
isStop = False
for key,value in questionsDict.items():
    #print(key,value)
    for key1, value1 in value.items():
        #print(key1,value1)
        if key1 == 'question':
            print(value1)
        if key1 == 'answers':
            for key2, value2 in value1.items():
                print (key2, '->', value2)
        if key1 == 'result':
            resultAnswer = int(value1)
            print(resultAnswer, '-> правильный ответ')
    print('Ваш ответ')
    userInput = userNum()
    if isStop:
        break
    else:
        if userInput == resultAnswer:
            print('Правильный ответ')
            sum += 1000
            print('Ваш выигрыш =', sum)
        else:
            print('Игра окончена, вы проиграли')
            sum = 0
            break
print('Ваш итоговый выигрыш =', sum)
