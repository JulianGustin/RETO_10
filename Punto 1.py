def calcular_promedio(arreglo:list)->float:
    if len(arreglo)==0: #Si el arreglo no tiene numeros, evita dividir por cero
        return 0
    suma = 0
    for num in arreglo:
        suma+=num #Sumar los números dentro del arreglo
    promedio = suma/len(arreglo) #Dividirlos por la cantidad de números en el arreglo
    return promedio

def ingresar_lista(): #Ingresar la lista por input
    arreglo = [] #Inicializar el arreglo
    while True:
        try:
            tamaño = int(input("Ingresa el tamaño del arreglo: "))
            if tamaño > 0: #Si el tamaño de la lista no es 0, continua.
                break 
            else: #Si el tamaño de la lista es 0, reinicia
                print("Ingrese un número mayor a 0")
        except ValueError: #Si ingresa un valor no numérico, reinicia
            print("Ingresa un número entero: ")

    for i in range(tamaño): #Itera las veces indicadas en el tamaño de la lista
        while True:
            try:
                num = float(input(f"Ingresa el número {i+1}: "))
                arreglo.append(num) #Ingresa el número a la lista
                break
            except ValueError: #Si no es un valor numérico, reinicia
                print("Ingresa un número real")
    return arreglo

if __name__ == "__main__":
    arreglo = ingresar_lista()
    promedio = calcular_promedio(arreglo)
    print("El promedio del arreglo es:", promedio)

