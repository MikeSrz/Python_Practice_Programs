acum=1
#numeros = [ (acum := acum * i) for i in range(1,4)]
numeros = (j:= acum/j) for j in range ([(acum := acum * i) for i in range(1,4)])
print (numeros)
