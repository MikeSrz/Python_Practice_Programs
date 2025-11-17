def calculateFactorial(n): 
    if n == 0:
        return 1
    return n*calculateFactorial(n-1)

def is_prime(n):
    if n <= 0:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0):
        return False
    else:
        for i in range(3, int(math.sqrt(n)), 2):
            if n % i == 0:
                return False
        return True


#si a es positivo y b es mayor que -4ac => CASO A
#para manejar 0s seguirá otro flujo de cálculo. => CASO C, despejamos la ecuacion y calculamos
#si b^2 es menor que -4ac => CASO B

def calc_2grade_ec(a, b, c):
    # CASO B: discriminante negativo
    if a != 0 and b**2 - 4*a*c < 0:
        return None, None

    # CASO C: ecuación lineal o c = 0
    elif a == 0 or c == 0:
        if a == 0:
            if b != 0:
                x1 = -c/b
                x2 = None
            else:
                x1 = None
                x2 = None  
            return x1, x2
        else: 
            x1 = -b/a
            x2 = 0
            return x1, x2

    # CASO A: ecuación cuadrática
    else:
        discriminant = math.sqrt(b**2 - 4*a*c)
        x1 = (-b + discriminant) / (2*a)
        x2 = (-b - discriminant) / (2*a)
        return x1, x2