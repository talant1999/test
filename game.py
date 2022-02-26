import random


def randNum():
    numList = []
    while len(numList) < 4:
        num = random.randint(0,9)
        if num in numList:
            continue
        else:
            numList.append(num)
    return numList


def userNum():
    myNumList = []
    while len(myNumList) < 4:
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
                    myNumList.append(num)
            except Exception:
                print('Вы ввели не цифру')
                continue
    return myNumList


isStop = False
while not isStop:
    # isFoundNum = False
    randCalcNum = randNum()
    userCalcNum = userNum()
    print(randCalcNum)
    if not isStop:
        isFoundNum = False
        while not isFoundNum and not isStop:
            i = 0
            letterK = 0
            letterB = 0
            while i < 4:
                if randCalcNum[i] == userCalcNum[i]:
                    letterK = letterK + 1
                    i += 1
                    continue
                elif randCalcNum[i] in userCalcNum:
                        letterB = letterB + 1
                        i += 1
                        continue
                else:
                    i += 1
                    continue
            if letterK == 4:
                isFoundNum = True
                print('Верно, вы угадали число')
            else:
                print('К = ', letterK, 'Б = ', letterB)
                userCalcNum = userNum()
                if isStop:
                    break
                else:
                    continue
    else:
        break
print()
print('Ваша игра закончена')
