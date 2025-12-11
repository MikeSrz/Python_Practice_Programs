x = 1
y = 2

#Swap con xor

#111XOR192 => RESULTADO
#resultadoXORMILLAVE HERMANO => MICONTRSELA
#RESULTADO 82828XOR2882XOR999XOR0001 =>
#111XOR111 => 0
#111XOR0 => 111
# =>
x = x ^ y
y = y ^ x
x = y ^ x

print(x)
print(y)