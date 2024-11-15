
#creamos la varible con la que se le va apreguntar al usario si quiere volver a ejecutar el programa y la inicializamo a que "si"
continuar = "s"

while continuar == "s":

    # Solicitamos 10 numeros al usuario
    numeros = []
    print("Introduce 10 numeros:")
    for i in range(10):
        num = int(input(f"Numero {i + 1}: "))
        numeros.append(num)

    # Calculamos los cuadrados
    cuadrados = []
    for num in numeros:
        #para calular el cuadreda se hace con **
        cuadrados.append(num ** 2)

    # Mostramos resultados
    for i in range(10):
        print(f"El numero en la posicion {i} es {numeros[i]} y su cuadrado es {cuadrados[i]}")

    # Preguntamos si desea reiniciar o salir
    continuar = input("¿Quieres iniciar el proceso de nuevo? (s/n): ").strip().lower()

print("Gracias por usar el programa. Sayonara!")
