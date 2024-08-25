# RETO_10
Reto 10 de la clase PDC
***
## Punto 1
Calcular el promedio de un arreglo de reales
```python
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
```
***
## Punto 2
Calcular el producto punto de dos arreglos (Vectores) de igual tamaño
```python
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
```
***
## Punto 3
Algoritmo que deja al final de una lista todos los ceros dentro de ella
```python
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
```
***
