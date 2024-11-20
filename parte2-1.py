def descuento(precio, porcentaje_descuento=10):
    return precio - (precio * (porcentaje_descuento / 100))

precio = int(input("Ingrese el precio: "))
desc = input("Ingrese el descuento (descuento predeterminado del 10%): ")

if desc:
    desc = int(desc)
    print(f"El precio final es: {descuento(precio, desc)}")
else:
    print(f"El precio final con descuento predeterminado es: {descuento(precio)}")


