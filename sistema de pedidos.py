def registrar_cliente(clientes, id_cliente, nombre, correo):

    if id_cliente in clientes:
        return clientes, "Ese cliente ya existe."

    clientes[id_cliente] = {
        "nombre": nombre,
        "correo": correo
    }
    return clientes, "Cliente registrado correctamente."


def registrar_producto(productos, id_producto, nombre_producto, precio_unitario):
    if id_producto in productos:
        return productos, "Ese producto ya existe."

    productos[id_producto] = (id_producto, nombre_producto, precio_unitario)
    return productos, "Producto registrado correctamente."


def crear_pedido(pedidos, id_pedido, id_cliente, id_producto, cantidad, clientes, productos):
    if id_pedido in pedidos:
        return pedidos, "Ese pedido ya existe."

    if id_cliente not in clientes:
        return pedidos, "El cliente no está registrado."

    if id_producto not in productos:
        return pedidos, "El producto no está registrado."

    if cantidad <= 0:
        return pedidos, "La cantidad debe ser mayor que cero."

    producto = productos[id_producto]
    precio_unitario = producto[2]
    total_pedido = precio_unitario * cantidad

    pedidos[id_pedido] = {
        "id_cliente": id_cliente,
        "id_producto": id_producto,
        "cantidad": cantidad,
        "total": total_pedido
    }

    return pedidos, "Pedido creado correctamente."


def consultar_pedidos(pedidos, clientes, productos):
    if len(pedidos) == 0:
        return "\nNo hay pedidos registrados."

    texto = "\n=== PEDIDOS REGISTRADOS ===\n"

    for id_pedido, info_pedido in pedidos.items():
        nombre_cliente = clientes[info_pedido["id_cliente"]]["nombre"]
        nombre_producto = productos[info_pedido["id_producto"]][1]
        cantidad = info_pedido["cantidad"]
        total = info_pedido["total"]

        texto += (
            f"\nPedido: {id_pedido}\n"
            f"Cliente: {nombre_cliente}\n"
            f"Producto: {nombre_producto}\n"
            f"Cantidad: {cantidad}\n"
            f"Total: {total}\n"
            f"-------------------------\n"
        )

    return texto


def calcular_ingresos_del_dia(pedidos):
    ingresos = 0

    for pedido in pedidos.values():
        ingresos += pedido["total"]

    return ingresos


def generar_reporte_final(pedidos, clientes, productos):
    total_pedidos = len(pedidos)
    ingresos_totales = calcular_ingresos_del_dia(pedidos)

    reporte = "\n=== REPORTE FINAL ===\n"
    reporte += f"Total de pedidos registrados: {total_pedidos}\n"
    reporte += f"Total de ingresos generados: {ingresos_totales}\n"

    reporte += "\nPedidos agrupados por cliente:\n"

    for id_cliente, datos_cliente in clientes.items():
        nombre_cliente = datos_cliente["nombre"]
        reporte += f"\n{nombre_cliente}: "

        encontro_pedidos = False

        for pedido in pedidos.values():
            if pedido["id_cliente"] == id_cliente:
                nombre_producto = productos[pedido["id_producto"]][1]
                cantidad = pedido["cantidad"]
                reporte += f"{nombre_producto} (x{cantidad}) "
                encontro_pedidos = True

        if not encontro_pedidos:
            reporte += "No realizó pedidos."

    reporte += "\n\nProductos vendidos durante el día:\n"

    for pedido in pedidos.values():
        nombre_producto = productos[pedido["id_producto"]][1]
        reporte += f"- {nombre_producto}\n"

    return reporte


def mostrar_menu():
    return input(
        "\n=== SISTEMA DE GESTIÓN DE PEDIDOS ===\n"
        "1. Registrar cliente\n"
        "2. Registrar producto\n"
        "3. Crear pedido\n"
        "4. Consultar pedidos\n"
        "5. Calcular ingresos del día\n"
        "6. Generar reporte final\n"
        "7. Salir\n"
        "Seleccione una opción: "
    )


def main():
    clientes = {}
    productos = {}
    pedidos = {}

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            id_cliente = int(input("Ingrese el ID del cliente: "))
            nombre = input("Ingrese el nombre del cliente: ")
            correo = input("Ingrese el correo del cliente: ")
            clientes, mensaje = registrar_cliente(clientes, id_cliente, nombre, correo)
            print(mensaje)

        elif opcion == "2":
            id_producto = int(input("Ingrese el ID del producto: "))
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_unitario = float(input("Ingrese el precio del producto: "))
            productos, mensaje = registrar_producto(productos, id_producto, nombre_producto, precio_unitario)
            print(mensaje)

        elif opcion == "3":
            id_pedido = int(input("Ingrese el ID del pedido: "))
            id_cliente = int(input("Ingrese el ID del cliente: "))
            id_producto = int(input("Ingrese el ID del producto: "))
            cantidad = int(input("Ingrese la cantidad: "))
            pedidos, mensaje = crear_pedido(
                pedidos, id_pedido, id_cliente, id_producto, cantidad, clientes, productos
            )
            print(mensaje)

        elif opcion == "4":
            print(consultar_pedidos(pedidos, clientes, productos))

        elif opcion == "5":
            print(f"\nLos ingresos totales del día son: {calcular_ingresos_del_dia(pedidos)}")

        elif opcion == "6":
            print(generar_reporte_final(pedidos, clientes, productos))

        elif opcion == "7":
            return "Programa finalizado."

        else:
            print("Opción inválida. Intente nuevamente.")


print(main())