catalogo = {
    "Camiseta": 20,
    "Jeans": 40,
    "Zapatos": 60,
    "Sombrero": 10
}

carrito = []
contador = 1 # Inicializamos el contador en 1
contraseña = "Thel"
usuario = "prof"

print("Tienes 3 intentos para ingresar al sistema")

while contador <= 3:
    print("Hola, por favor ingresa tu usuario para poder entrar al sistema")
    usuario_usuario = input()

    print("Hola, por favor ingresa tu contraseña  para poder entrar al sistema")
    contraseña_usuario = input()

    if contraseña == contraseña_usuario and usuario == usuario_usuario:
        print("Bienvenido a la Tienda Virtual")
        break # Si el usuario y la contraseña son correctos, salimos del bucle
    else:
        print("Usuario o contraseña incorrectos, intenta nuevamente.")
        contador += 1 # Incrementamos el contador

if contador > 3:
    print("Has excedido el número de intentos permitidos. El sistema se cerrará.")
    exit() # Agregamos un exit() para que el programa se detenga después de 3 intentos fallidos

while True:
    print("\nMenú:")
    print("1. Agregar productos al carrito")
    print("2. Ver carrito")
    print("3. Realizar el pago y salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\nProductos disponibles:")
        for producto, precio in catalogo.items():
            print(f"• {producto} ${precio}")
        producto = input("Ingrese el nombre del producto que desea agregar: ").title()

        if producto in catalogo:
            carrito.append(producto)
            print(f"Producto '{producto}' agregado al carrito.")
        else:
            print(f"El producto '{producto}' no existe en el catálogo.")

    elif opcion == "2":
        print("\nCarrito:")
        if not carrito:
            print("El carrito está vacío.")
        else:
            for producto in set(carrito):
                cantidad = carrito.count(producto)
                precio_unitario = catalogo[producto]
                print(f"{cantidad} {producto} - ${precio_unitario} c/u")

    elif opcion == "3":
        total_a_pagar = sum(catalogo[producto] for producto in carrito)
        print(f"Total a pagar: ${total_a_pagar}")

        if total_a_pagar == 0:
            print("No hay productos en el carrito. Gracias por su visita.")
            break
        
        while True: # Loop para asegurar que se ingrese un monto válido
            try:
                monto_pagado = float(input("Ingrese el monto con el que pagará: "))
                if monto_pagado < 0:
                    print("El monto ingresado no puede ser negativo. Por favor, ingrese un monto válido.")
                    continue  # Regresa al inicio del loop while interno
                cambio = monto_pagado - total_a_pagar
                
                if cambio >= 0:
                    mensaje_cambio = f"Su cambio es: ${round(cambio, 2)}" if cambio > 0 else "¡Exacto! No se requiere cambio."
                    print(f"Gracias por su compra. {mensaje_cambio}")
                    break # Sale del loop while interno
                else:
                    print("El monto ingresado es insuficiente. Por favor, ingrese un monto válido.")
            except ValueError:
                print("Monto inválido. Por favor, ingrese un monto numérico válido.")
        break # Sale del loop while principal (del menú)
