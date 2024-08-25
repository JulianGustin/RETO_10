def producto_punto(arreglo_1:list, arreglo_2:list)->int:
    if len(arreglo_1) != len(arreglo_2):
        return None #Si las listas no son de igual tamaño, retorna none
    total = 0
    for i in range(len(arreglo_1)): #Itera las veces del tamaño de la lista
        total += arreglo_1[i] * arreglo_2[i] #Suma el producto de los numeros i de cada lista
    return total

def ingresar_lista(): #Funcion de ingresar lista, ya definida en el punto 1
    arreglo = []
    while True:
        try:
            tamaño = int(input("Ingresa el tamaño del arreglo(Debe ser igual para los dos): "))
            if tamaño > 0: 
                break
            else:
                print("Ingrese un número mayor a 0")
        except ValueError:
            print("Ingresa un número entero: ")

    for i in range(tamaño):
        while True:
            try:
                num = float(input(f"Ingresa el número {i+1}: "))
                arreglo.append(num)
                break
            except ValueError:
                print("Ingresa un número real")
    return arreglo

if __name__ == "__main__":
    arreglo_1 = ingresar_lista()
    arreglo_2 = ingresar_lista()
    resultado = producto_punto(arreglo_1,arreglo_2)
    if resultado is None: #Si es none, se acaba el programa.
        print("Los vectores tienen tamaño diferente")
    else:
        print (f"El producto de el arreglo {arreglo_1} y el arreglo {arreglo_2} es {resultado}")