def countColLineMatrix(fileNameLocal):
    with open(fileNameLocal, 'r') as file:
        i = 0
        j = 0
        for line in file:
            i += 1
            if j > 0:
                continue
            else:
                mas = line.split(' ')
                for elem in mas:
                    if elem != '\n':
                        j += 1
    return i,j


def createMatrix(lineLocal,colLocal):
    matrixLocal = []
    for i in range(lineLocal):
        matrixLocal.append([0]*colLocal)
    return matrixLocal


def powMatrix(matrixLocal, fileNameLocal):
    with open(fileNameLocal, 'r') as file:
        i = 0
        for line in file:
            i += 1
            j = 0
            mas = line.split(' ')
            for item in mas:
                j += 1
                if item != '\n':
                    matrix[i - 1][j - 1] = int(item) ** i
    return matrixLocal


def showMatrix(matrixLocal):
    for line in matrixLocal:
        for item in line:
            print(item, end=' ')
        print()


def addLineCol(lineLocal, colLocal, matrixLocal, matrixOutputLocal):
    for i in range(lineLocal+1):
        sumLine = 0
        for j in range(colLocal+1):
            try:
                sumLine += matrixLocal[i][j]
                matrixOutputLocal[i][j] = matrixLocal[i][j]
            except:
                matrixOutputLocal[i][j] = sumLine
    for i in range(colLocal+1):
        sumCol = 0
        for j in range(lineLocal+1):
            try:
                sumCol += matrixLocal[j][i]
            except:
                continue
        matrixOutputLocal[j][i] = sumCol
    return matrixOutputLocal


def writeMatrixInFile(matrixLocal, fileNameLocal):
    file = open(fileNameLocal, 'w')
    for line in matrixLocal:
        s = ''
        for item in line:
            s += str(item) + ' '
        file.write(s + '\n')
    file.close()


matrix = [
    [2,3,4],
    [5,6,7],
    [3,2,6]
]
fileName = 'matrix1.txt'
print('Начальная матрица')
showMatrix(matrix)
writeMatrixInFile(matrix,fileName)
line, col = countColLineMatrix(fileName)
matrix = createMatrix(line,col)
matrix = powMatrix(matrix, fileName)
print('Матрица со степенями')
showMatrix(matrix)
matrix2 = createMatrix(line+1,col+1)
matrix2 = addLineCol(line,col,matrix, matrix2)
print('Матрица с дополнительными строкой и столбцом')
showMatrix(matrix2)
writeMatrixInFile(matrix2,fileName)
