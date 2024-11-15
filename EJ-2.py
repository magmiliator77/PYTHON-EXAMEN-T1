#Para ello importamos la libreria  random

import random;

# Generaramos 10 números aleatorios entre 0 y 100
numeros = [random.randint(0, 100) for i in range(10)]

# Encontrar el máximo y el mínimo
maximo = max(numeros)
minimo = min(numeros)

# Encontrar las posiciones del máximo y el mínimo
posiciones_maximo = []
posiciones_minimo = []


#Aqui mediante las dos variables creadas anteriormente "posiciones_maximo" "posiciones_minimo" estamos diciendo que si los numeros generados en "numeros" cogemos el mayor y lo añadiemos a la "posiciones_maximo mediante append, lo mismo para el minimo"
for i in range(len(numeros)):

    if numeros[i] == maximo:
        posiciones_maximo.append(i)

    if numeros[i] == minimo:
        posiciones_minimo.append(i)



# Mostramos los resultados
print("Números generados:", numeros)

print(f"Máximo: {maximo}, en las posiciones: {posiciones_maximo}")

print(f"Mínimo: {minimo}, en las posiciones: {posiciones_minimo}")
