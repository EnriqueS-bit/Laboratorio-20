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

