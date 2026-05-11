menu = True
deuda = 100000

while menu:
    print("--MENU--")
    print("1. Pago tarjeta de crédito")
    print("2. Simulación compras")
    print("3. Salir")
    op = int(input("Seleccione una opción: "))

    if op == 1:
        print("Pago tarjeta de crédito.")
        pago = int(input("Ingrese monto de pago: "))
        if pago >= 0:
            if pago <= deuda:
                deuda = deuda - pago
                print(f"Pago exitoso, su deuda es de: ${deuda}")
            else:
                print("Pago excede la deuda.")

    elif op == 2:
        print("Simulador de compras")
    elif op == 3:
        menu = False
    
