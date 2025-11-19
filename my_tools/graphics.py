#Autor: MikeSrz
#
#Descripción: Módulo de dibujo de gráficos y formas.

import time

def create_square(height, width, fill=True, tabs=0):
    square = []
    for i in range (height):
        square.append([])
        for j in range (width+tabs):
            square[i].append(False)
            if i == 0 or i == (height-1):
                #Una excepción en la primera fila y en la última
                square[i][j] = (j >= tabs)
                continue

            if fill:
                square[i][j] = (j >= tabs)
            else:
                    square[i][j] = (j == tabs or j == (width+tabs-1))

    return square

def create_triangle(height, fill=True, tabs=0):
    triangle = []
    width = ((height-1)*2+1)
    top = int(width/2)+tabs
    left = top
    right = top

    for i in range (height):
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
                triangle[i][j] = (left <= j and right >= j)
            else:
                triangle[i][j] = (left == j or right == j)
                 
        left = left-1
        right = right+1

    return triangle

def create_itriangle(height, fill=True, tabs=0):
        triangle = []
        width = ((height-1)*2+1)
        top = int(width/2)+tabs
        left = tabs
        right = width+tabs-1

        for i in range (height):
            triangle.append([])
            for j in range (width+tabs):
                triangle[i].append(False)
                if i == height-1:
                    triangle[i][j] = (j == top)
                    continue
            
                if i == 0:
                    triangle [i][j] = (j >= tabs)
                    continue

                if fill:
                        triangle[i][j] = (left <= j and right >= j)
                else:
                    triangle[i][j] = (left == j or right == j)

            left = left+1
            right = right-1

        return triangle

def print_figure(figure, relleno="*"):
    for i in range(len(figure)):
        for j in range(len(figure[1])):
            if figure[i][j]:
                print(relleno, end="")
            else:
                print(" ", end="")
        print()


def main():
    square = create_square(10, 10, True, 10)
    triangle = create_itriangle(10, True, 20)
    print_figure(triangle, "/")

    for i in range (1000):
        time.sleep(0.5)
        #Me haría falta refrescar la pantalla
        triangle = create_itriangle(10, True,i)
        print_figure(triangle)

if __name__ == "__main__":
    main()