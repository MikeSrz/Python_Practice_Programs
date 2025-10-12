def drawSquare(height, width, fill=True, tabs=0):
    #Cuadrado relleno: Pintando linea a linea
    if fill == True:
        for i in range (0, height):
            #Vaciamos el string que pinta.
            graph = ""
            for j in range (0, width):
                graph += "*" 

            print(graph)
   #Cuadrado vacío
    else:
        for i in range (0, height):
            #Vaciamos el string que pinta.
            graph = ""
            if i == 0 or i == height-1:
                for j in range (0, width):
                    graph += "*"
            else:
                for j in range (0, width):
                    if j == 0 or j == width-1:
                        graph += "*"
                    else:
                        graph += " "

            print (graph)

def drawTriangle(height, width, tabs=0):
    #Creamos array vacío
    #Tabs Es el desplazamiento.
    positions_to_paint = []
    for i in range (0, (width+tabs)):
        positions_to_paint.append(0)

    top = int((width)/2+tabs)
    positions_to_paint[top-1] += top

    for i in range (0, height):
        graph = ""
        for j in range (1, ((width+tabs)+1)):
            if j in positions_to_paint:
                graph += "*"
            else:
                    graph += " "

        #Añadiendo números a la lista, en cada ciclo se añade uno por arriba y otro por abajo.
        if i < (width/2)+tabs:
            if i == 0:
                topLast = top+1
                topFirst = top-1
                positions_to_paint[topFirst-1] += topFirst
                positions_to_paint[topLast-1] += topLast

            else:
                topLast = topLast+1
                topFirst = topFirst-1
                positions_to_paint[topFirst-1] += topFirst
                positions_to_paint[topLast-1] += topLast

        print(graph)
        print (positions_to_paint)


drawTriangle(1500,2000,50)

