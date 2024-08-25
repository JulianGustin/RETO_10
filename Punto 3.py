def mover_ceros(arreglo:list)->list:
    lista_sin_0 = [x for x in arreglo if x !=0] #Hace una lista con todos los números del arreglo que no sean 0.
    contador_ceros = len(arreglo) - len(lista_sin_0) #Encuentra la diferencia de la cantidad de numeros en la lista completa y en la lista sin ceros, para obtener el número de ceros
    lista_final = lista_sin_0 + [0] * contador_ceros #Añade todos los ceros al final
    return lista_final

def ingresar_lista(): #Ingresar lista por input
    arreglo = []
    while True:
        try:
            tamaño = int(input("Ingresa el tamaño del arreglo: "))
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
    arreglo = ingresar_lista()
    print("Su lista es: ", arreglo)
    arreglo = mover_ceros(arreglo)
    print("Su lista con los ceros al final: ", arreglo)