menu = True

while menu:
    print("--MENU--")
    print("1. Pago tarjeta de crédito")
    print("2. Simulación compras")
    print("3. Salir")
    op = int(input("Seleccione una opción: "))

    if op == 1:
        print("Pago tarjeta de crédito.")
    elif op == 2:
        print("Simulador de compras")
    elif op == 3:
        menu = False
    
    