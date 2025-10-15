#Autor: MikeSrz
#Fecha: 15/10/2025
#Descripción: Dibujando figuras 2D usando matrices.

def generateSquare(height, width, fill=True):
    square = []
    for i in range (height):
        #Generando fila
        square.append([])
        for j in range (width):
            #Generando columna
            if i == 0:
                square[i].append(True)
                continue
            if i == (width):
                square[i].append(True)
                continue

            if fill:
                square[i].append(True)
            else:
                if j == 0 or j == (width-1):
                    square[i].append(True)
                else:
                    square[i].append(False)
    return square

def generateTriangle(height, fill=True):
    triangle = []
    width = ((height-1)*2+1)
    top = int(width/2)
    left = top
    right = top

    for i in range (height):
        #Generando Fila
        triangle.append([])
        for j in range (width):
            triangle[i].append(False)
            if i == 0:
                triangle[i][j] = (j == top)
                continue
            
            if i == height-1:
                triangle [i][j] = True
                continue

            if fill:
                if left <= j and right >= j:
                    triangle[i][j] = True
            else:
                if left == j or right == j:
                    triangle[i][j] = True
                 
        left = left-1
        right = right+1

    return triangle
                

def printFigure(figure, relleno="*"):
    for i in range(len(figure)):
        for j in range(len(figure[1])):
            if figure[i][j]:
                print(relleno, end="")
            else:
                print(" ", end="")
        print()


square = generateSquare(2,2,True)
triangle = generateTriangle(4, False)
printFigure(triangle) 
printFigure(generateTriangle(6))
printFigure(generateSquare(8,5))
