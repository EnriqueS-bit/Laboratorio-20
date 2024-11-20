#Parte 1-1
def mensaje(nombre):
    print(f"Hola, {nombre} Bienvenido.")
    
nombre=input("Ingrese su nombre: ")
mensaje(nombre)
    
#Parte 1-2
def area_circulo(radio):
    import math
    return math.pi * radio ** 2
radio=int(input("Ingrese el radio del circulo: "))
print("El area del circulo es: ",area_circulo(radio))

#Parte 3
def mayor_valor(*numeros):
    return max(numeros)
numeros = []
cantidad = int(input("¿Cuántos números deseas ingresar? "))
for _ in range(cantidad):
    numero = float(input("Ingresa un número: "))
    numeros.append(numero)
print("Números ingresados:", numeros)
mayor = mayor_valor(*numeros)
print(f"El mayor valor es: {mayor}")

#Parte 4-1
def suma(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma
    
def mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    return may
    
def menor(lista):
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]<men:
            men=lista[x]
    return men
    
listaoriginal=[23,56,12,47,89,85,100,63,97,2,852]
print("Lista original: ",listaoriginal)
print("La suma de los elemnetos de la lista es: ",suma(listaoriginal))
print("El valor mayor de la lista es: ", mayor(listaoriginal))
print("El valor menor de la lista es: ",menor(listaoriginal))

#Parte 4-2
def mascaracteres(palabras):
    pos=0
    for x in range(len(palabras)):
        if len(palabras[x]) > len(palabras[pos]):
            pos=x 
    return palabras[pos]

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio","Septiembre", "Diciembre"]
print("Palabra con mas caracteres:",mascaracteres(palabras))