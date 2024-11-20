def area_circulo(radio):
    import math
    return math.pi * radio ** 2
radio=int(input("Ingrese el radio del circulo: "))
print("El area del circulo es: ",area_circulo(radio))