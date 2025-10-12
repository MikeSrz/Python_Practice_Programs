def drawSquare(height, width, fill=True, tabs=0):
    #Cuadrado relleno: Pintando linea a linea
    if fill:
        for i in range (0, height):
            #Vaciamos el string que pinta.
            graph = ""
            for tab in range (0, tabs):
                graph += " " 
                
            for j in range (0, width):
                graph += "*"
            print(graph)

   #Cuadrado vacío
    else:
        for i in range (0, height):
            #Vaciamos el string que pinta.
            graph = ""
            if i == 0 or i == height-1:
                for tab in range (0, tabs):
                    graph += " "
                for j in range (0, width):
                    graph += "*"

            else:
                for tab in range(0,tabs):
                    graph += " "
                for j in range (0, width):
                    if j == 0 or j == width-1:
                        graph += "*"
                    else:
                        graph += " "

            print (graph)

def drawTriangle(height, fill=True, tabs=0):
    #Sumar 1 al final del todo era necesario para los bucles.
    width = ((height-1)*2+1)+1 
    #Creamos array vacío y lo iniciamos con Falses.
    positions_to_paint = []
    for i in range (0, width+tabs):
        positions_to_paint.append(False)
    
    top = int((width/2)+tabs) 
    positions_to_paint[top-1] = True
    #pintando triángulo.
    for i in range (0, height):
        graph = ""
        #pintamos los que sean True
        for j in positions_to_paint:
            if j == True:
                graph += "*"
            else:
                graph += " "
        print (graph)

        #Marcamos como True aquellos que queremos pintar en la próxima iteración de i
        if i == 0:
            right = top+1
            left = top-1
            positions_to_paint[right-1] = True
            positions_to_paint[left-1] = True
            positions_to_paint[top-1] = True if fill else  False

        elif i == height-2:
            #Último ciclo:
            for j in range (left-2, right+1):
                positions_to_paint[j] = True
                 
        else:
            right = right+1
            left = left-1
            #Ponemos en False las casillas anteriores para que no se pinten en caso fill false
            positions_to_paint[right-2] = True if fill else False
            positions_to_paint[left] = True if fill else  False
            positions_to_paint[right-1] = True
            positions_to_paint[left-1] = True

    

drawTriangle (7,True,15)
drawTriangle(8,False,14)
drawTriangle(12,False, 10)
drawSquare(7,12,False,15)

