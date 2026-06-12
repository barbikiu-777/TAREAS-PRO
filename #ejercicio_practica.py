#ejercicio_practica

def calcular_subtotal(valor_noche, cantidad_noches):
    return valor_noche * cantidad_noches

def calcular_descuento(subtotal):
    if subtotal>=200000:
        return subtotal * 0.20
    elif 200000>subtotal>=100000:
        return subtotal * 0.10
    else:
        return 0

def calcular_impuesto(subtotal, descuento):
    monto = subtotal - descuento
    return monto * 0.08

def calcular_total(subtotal, descuento, impuesto):
    return subtotal - descuento + impuesto

def mostrar_resumen(nombre_cliente, valorxnoche, cantnoches, subtotal, descuento, impuesto, total):
    print("---RESUMEN DE RESERVA---")
    print(f"Cliente: {nombre_cliente} ")
    print(f"Valor por noche: ${valorxnoche}")
    print(f"Cantidad de noches: {cantnoches}")
    print(f"Subtotal: ${subtotal}")
    print(f"Descuento: ${descuento}")
    print(f"Impuesto turistico: ${impuesto}")
    print(f"Total a pagar: {total}")
    print("--------------------------")

ingresos_acumulados= 0

while True:

    print("\n---RESERVAS DE HOTEL---")
    print("1. Registrar reserva")
    print("2. Mostrar ingresos acumulados")
    print("3. Salir")

    try:
        opcion= int(input("Seleccione una opcion: "))

        if opcion==3:
            print("Saliendo del sist de reservas...")
            break

        elif opcion==1:
            nombre= input("Ingrese su nombre: ")
            valor= int(input("Ingrese el valor de la noche: $"))
            cantidad= int(input("Ingrese cantidad de noches a reservar: "))

            if cantidad<=0 or valor<=0:
                print("ERROR: Ingrese solo numeros positivos y mayores a 0")

            else:
                subtotal= calcular_subtotal(valor,cantidad)
                descuento= calcular_descuento(subtotal)
                impuesto= calcular_impuesto(subtotal, descuento)
                total= calcular_total(subtotal, descuento, impuesto)

                ingresos_acumulados += total

                mostrar_resumen(nombre,
                valor,
                cantidad,
                subtotal,
                descuento,
                impuesto,
                total)

        elif opcion==2:
            print(f"Los ingresos acuculados son: {ingresos_acumulados}")

        else:
            print("Ingrese una opcion validad")

    except ValueError:
        print("ERROR: ingrese numeros validos")




