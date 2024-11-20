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




    