def createSquare(height, width, fill=True, tabs=0):
    square = []
    for i in range (height):
        #Generando fila
        square.append([])
        for j in range (width+tabs):
            square[i].append(False)
            #Generando columna
            if i == 0 or i == width:
                square[i][j] = (j >= tabs)
                continue

            if fill:
                square[i][j] = (j >= tabs)
            else:
                if j == 0 or j == (width-1):
                    square[i][j] = True
    return square

def createTriangle(height, fill=True, tabs=0):
    triangle = []
    width = ((height-1)*2+1)
    top = int(width/2)+tabs
    left = top
    right = top

    for i in range (height):
        #Generando Fila
        triangle.append([])
        for j in range (width+tabs):
            triangle[i].append(False)
            if i == 0:
                triangle[i][j] = (j == top)
                continue
            
            if i == height-1:
                triangle [i][j] = (j >= tabs)
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

    def createInvertedTriangle(height, fill=True, tabs=0):
    triangle = []
    width = ((height-1)*2+1)
    top = int(width/2)+tabs
    left = tabs
    right = width+tabs-1

    for i in range (height):
        #Generando Fila
        triangle.append([])
        #Generando columnas
        for j in range (width+tabs):
            triangle[i].append(False)
            if i == height-1:
                triangle[i][j] = (j == top)
                continue
            
            if i == 0:
                triangle [i][j] = (j >= tabs)
                continue

            if fill:
                if left <= j and right >= j:
                    triangle[i][j] = True
            else:
                if left == j or right == j:
                    triangle[i][j] = True
        left = left+1
        right = right-1

    return triangle

def printFigure(figure, relleno="*"):
    for i in range(len(figure)):
        for j in range(len(figure[1])):
            if figure[i][j]:
                print(relleno, end="")
            else:
                print(" ", end="")
        print()