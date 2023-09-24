
vector1 = [4,1,6,1,2,8,1,6]
vector2 = []
x = 5
for i in vector1:
    if i in range(-1,3): #escanea vector1 para detectar numeros mayores que -1 y menores que 3
        vector2.append(i)
print(vector2)
while vector2.count(5)<4:
    vector2.append(x) #comprueba que la cantidad de 5 es menor que 4 si es menor que 4 añade cincos
print(vector2)