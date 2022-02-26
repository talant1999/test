import socket
import time
import numpy as np
import random


def generateStr():
    arrWords = ['one', 'two', 'three', 'four', 'five']
    worsdList = np.random.choice(arrWords, random.randint(1, 9), True)

    newStr = listToString(worsdList)

    return newStr


def listToString(inputList):
    outputStr = ""
    for n in inputList:
        outputStr += n + " "

    return outputStr.rstrip()


sock = socket.socket()
sock.connect(('localhost', 9000))

n = 10
i = 0
while i <= n:
    try:
        text_to_send = generateStr()
        print(text_to_send)
        sock.send(text_to_send.encode())
        data = sock.recv(1024)
        print('>> ', data)
    except Exception as e:
        print('Exception: ', e)
        sock.close()
        break
    finally:
        i = i + 1
    time.sleep(2)

sock.close()
print('__END__')
