import socket


def wordCount(inputStr):
    wCount = dict()
    words = inputStr.split(" ")

    for word in words:
        if word in wCount:
            wCount[word] += 1
        else:
            wCount[word] = 1

    return wCount


sock = socket.socket()
sock.bind(('', 9000))
sock.listen(1)
conn, addr = sock.accept()

print('connected: ', addr)

while True:
    try:
        data = conn.recv(1024)
        print('> ', data)
        if not data:
            break
        wordCountDict = wordCount(data.decode("utf-8"))
        wordCountStr = str(wordCountDict)
        print(wordCountStr)
        conn.send(wordCountStr.encode())
    except Exception as e:
        print('Exception: ', e)
        conn.close()
        break

conn.close()
print('__END__')
sock.close()
