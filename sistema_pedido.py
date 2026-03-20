"""
Sistema de Gestión de Pedidos de Clientes
Solución del desafío construida usando solo diccionarios y tuplas.
No se usan listas en la lógica principal.
Todas las funciones reciben parámetros y retornan datos.
"""

def crear_datos_sistema(clientes_iniciales, productos_iniciales, pedidos_iniciales, contador_pedidos_inicial):
    """
    Crear el contenedor principal de datos del sistema.

    Args:
        clientes_iniciales (dict): Clientes registrados.
        productos_iniciales (dict): Productos registrados.
        pedidos_iniciales (dict): Pedidos registrados.
        contador_pedidos_inicial (int): Número del siguiente pedido.

    Returns:
        dict: Estructura de datos del sistema.
    """
    return {
        "clientes": clientes_iniciales,
        "productos": productos_iniciales,
        "pedidos": pedidos_iniciales,
        "contador_pedidos": contador_pedidos_inicial
    }


def validar_texto_no_vacio(valor, nombre_campo):
    """
    Validar que un valor de texto no esté vacío.

    Args:
        valor (str): Valor a validar.
        nombre_campo (str): Nombre del campo para retroalimentación.

    Returns:
        tuple: (bool, str)
    """
    valor_limpio = valor.strip()

    if valor_limpio == "":
        return False, f"{nombre_campo} no puede estar vacío."

    return True, valor_limpio


def validar_flotante_positivo(valor, nombre_campo):
    """
    Validar que un valor pueda convertirse en un número flotante positivo.

    Args:
        valor (str): Valor recibido.
        nombre_campo (str): Nombre del campo para retroalimentación.

    Returns:
        tuple: (bool, float|str)
    """
    try:
        numero = float(valor)
    except ValueError:
        return False, f"{nombre_campo} debe ser un número válido."

    if numero <= 0:
        return False, f"{nombre_campo} debe ser mayor que cero."

    return True, numero


def validar_entero_positivo(valor, nombre_campo):
    """
    Validar que un valor pueda convertirse en un entero positivo.

    Args:
        valor (str): Valor recibido.
        nombre_campo (str): Nombre del campo para retroalimentación.

    Returns:
        tuple: (bool, int|str)
    """
    try:
        numero = int(valor)
    except ValueError:
        return False, f"{nombre_campo} debe ser un número entero válido."

    if numero <= 0:
        return False, f"{nombre_campo} debe ser mayor que cero."

    return True, numero


def registrar_cliente(clientes, id_cliente, nombre_cliente, correo_cliente):
    """
    Registrar un cliente en el sistema.

    Args:
        clientes (dict): Diccionario de clientes.
        id_cliente (str): Identificador del cliente.
        nombre_cliente (str): Nombre del cliente.
        correo_cliente (str): Correo del cliente.

    Returns:
        tuple: (dict, str)
    """
    id_valido, id_verificado = validar_texto_no_vacio(id_cliente, "ID del cliente")
    if not id_valido:
        return clientes, id_verificado

    nombre_valido, nombre_verificado = validar_texto_no_vacio(nombre_cliente, "Nombre del cliente")
    if not nombre_valido:
        return clientes, nombre_verificado

    correo_valido, correo_verificado = validar_texto_no_vacio(correo_cliente, "Correo del cliente")
    if not correo_valido:
        return clientes, correo_verificado

    if id_verificado in clientes:
        return clientes, "El ID del cliente ya existe."

    clientes[id_verificado] = {
        "id_cliente": id_verificado,
        "nombre": nombre_verificado,
        "correo": correo_verificado
    }

    return clientes, f"Cliente '{nombre_verificado}' registrado correctamente."


def registrar_producto(productos, id_producto, nombre_producto, precio_unitario_texto):
    """
    Registrar un producto como una tupla.

    Args:
        productos (dict): Diccionario de productos.
        id_producto (str): Identificador del producto.
        nombre_producto (str): Nombre del producto.
        precio_unitario_texto (str): Precio unitario recibido en texto.

    Returns:
        tuple: (dict, str)
    """
    id_valido, id_verificado = validar_texto_no_vacio(id_producto, "ID del producto")
    if not id_valido:
        return productos, id_verificado

    nombre_valido, nombre_verificado = validar_texto_no_vacio(nombre_producto, "Nombre del producto")
    if not nombre_valido:
        return productos, nombre_verificado

    precio_valido, precio_verificado = validar_flotante_positivo(precio_unitario_texto, "Precio unitario")
    if not precio_valido:
        return productos, precio_verificado

    if id_verificado in productos:
        return productos, "El ID del producto ya existe."

    productos[id_verificado] = (id_verificado, nombre_verificado, precio_verificado)

    return productos, f"Producto '{nombre_verificado}' registrado correctamente."


def calcular_total_pedido(precio_unitario, cantidad):
    """
    Calcular el valor total de un pedido.

    Args:
        precio_unitario (float): Precio unitario.
        cantidad (int): Cantidad comprada.

    Returns:
        tuple: (float, str)
    """
    total = precio_unitario * cantidad
    return total, f"Total calculado: {total:.2f}"


def crear_pedido(pedidos, clientes, productos, contador_pedidos, id_cliente, id_producto, cantidad_texto):
    """
    Crear un pedido asociado a un cliente y un producto.

    Args:
        pedidos (dict): Diccionario de pedidos.
        clientes (dict): Diccionario de clientes.
        productos (dict): Diccionario de productos.
        contador_pedidos (int): Número del siguiente pedido.
        id_cliente (str): Identificador del cliente.
        id_producto (str): Identificador del producto.
        cantidad_texto (str): Cantidad recibida en texto.

    Returns:
        tuple: (dict, int, str)
    """
    cliente_valido, cliente_verificado = validar_texto_no_vacio(id_cliente, "ID del cliente")
    if not cliente_valido:
        return pedidos, contador_pedidos, cliente_verificado

    producto_valido, producto_verificado = validar_texto_no_vacio(id_producto, "ID del producto")
    if not producto_valido:
        return pedidos, contador_pedidos, producto_verificado

    cantidad_valida, cantidad_verificada = validar_entero_positivo(cantidad_texto, "Cantidad")
    if not cantidad_valida:
        return pedidos, contador_pedidos, cantidad_verificada

    if cliente_verificado not in clientes:
        return pedidos, contador_pedidos, "Cliente no encontrado."

    if producto_verificado not in productos:
        return pedidos, contador_pedidos, "Producto no encontrado."

    datos_cliente = clientes[cliente_verificado]
    datos_producto = productos[producto_verificado]
    total_pedido, _ = calcular_total_pedido(datos_producto[2], cantidad_verificada)

    id_pedido = f"PED-{contador_pedidos:03d}"

    pedidos[id_pedido] = {
        "id_pedido": id_pedido,
        "id_cliente": datos_cliente["id_cliente"],
        "nombre_cliente": datos_cliente["nombre"],
        "id_producto": datos_producto[0],
        "nombre_producto": datos_producto[1],
        "precio_unitario": datos_producto[2],
        "cantidad": cantidad_verificada,
        "total": total_pedido
    }

    return pedidos, contador_pedidos + 1, f"Pedido {id_pedido} creado correctamente."


def formatear_catalogo_clientes(clientes, titulo):
    """
    Construir una vista en texto de los clientes registrados.

    Args:
        clientes (dict): Diccionario de clientes.
        titulo (str): Título de la sección.

    Returns:
        tuple: (str, int)
    """
    reporte = titulo + "\n"
    reporte += "-" * len(titulo) + "\n"

    if len(clientes) == 0:
        reporte += "No hay clientes registrados.\n"
        return reporte, 0

    contador = 0
    for id_cliente in clientes:
        cliente = clientes[id_cliente]
        reporte += (
            f"ID: {cliente['id_cliente']} | "
            f"Nombre: {cliente['nombre']} | "
            f"Correo: {cliente['correo']}\n"
        )
        contador += 1

    return reporte, contador


def formatear_catalogo_productos(productos, titulo):
    """
    Construir una vista en texto de los productos registrados.

    Args:
        productos (dict): Diccionario de productos.
        titulo (str): Título de la sección.

    Returns:
        tuple: (str, int)
    """
    reporte = titulo + "\n"
    reporte += "-" * len(titulo) + "\n"

    if len(productos) == 0:
        reporte += "No hay productos registrados.\n"
        return reporte, 0

    contador = 0
    for id_producto in productos:
        producto = productos[id_producto]
        reporte += (
            f"ID: {producto[0]} | "
            f"Producto: {producto[1]} | "
            f"Precio unitario: {producto[2]:.2f}\n"
        )
        contador += 1

    return reporte, contador


def consultar_pedidos(pedidos, titulo):
    """
    Construir una cadena formateada con todos los pedidos.

    Args:
        pedidos (dict): Diccionario de pedidos.
        titulo (str): Título de la sección.

    Returns:
        tuple: (str, int)
    """
    reporte = titulo + "\n"
    reporte += "-" * len(titulo) + "\n"

    if len(pedidos) == 0:
        reporte += "No hay pedidos registrados.\n"
        return reporte, 0

    contador = 0
    for id_pedido in pedidos:
        pedido = pedidos[id_pedido]
        reporte += (
            f"Pedido: {pedido['id_pedido']} | "
            f"Cliente: {pedido['nombre_cliente']} | "
            f"Producto: {pedido['nombre_producto']} | "
            f"Cantidad: {pedido['cantidad']} | "
            f"Total: {pedido['total']:.2f}\n"
        )
        contador += 1

    return reporte, contador


def calcular_ingresos_diarios(pedidos, etiqueta):
    """
    Calcular los ingresos totales del día.

    Args:
        pedidos (dict): Diccionario de pedidos.
        etiqueta (str): Etiqueta para la respuesta.

    Returns:
        tuple: (float, str)
    """
    ingresos_totales = 0.0

    for id_pedido in pedidos:
        ingresos_totales += pedidos[id_pedido]["total"]

    return ingresos_totales, f"{etiqueta}: {ingresos_totales:.2f}"


def agrupar_pedidos_por_cliente(pedidos, titulo_seccion):
    """
    Agrupar la información de pedidos por cliente.

    Args:
        pedidos (dict): Diccionario de pedidos.
        titulo_seccion (str): Título de la sección.

    Returns:
        tuple: (str, dict)
    """
    pedidos_agrupados = {}
    for id_pedido in pedidos:
        pedido = pedidos[id_pedido]
        nombre_cliente = pedido["nombre_cliente"]

        if nombre_cliente not in pedidos_agrupados:
            pedidos_agrupados[nombre_cliente] = {
                "cantidad_pedidos": 0,
                "monto": 0.0,
                "detalles": ""
            }

        pedidos_agrupados[nombre_cliente]["cantidad_pedidos"] += 1
        pedidos_agrupados[nombre_cliente]["monto"] += pedido["total"]
        pedidos_agrupados[nombre_cliente]["detalles"] += (
            f"    - {pedido['id_pedido']}: {pedido['nombre_producto']} x {pedido['cantidad']} "
            f"= {pedido['total']:.2f}\n"
        )

    reporte = titulo_seccion + "\n"
    reporte += "-" * len(titulo_seccion) + "\n"

    if len(pedidos_agrupados) == 0:
        reporte += "No hay datos de clientes disponibles.\n"
        return reporte, pedidos_agrupados

    for nombre_cliente in pedidos_agrupados:
        info_cliente = pedidos_agrupados[nombre_cliente]
        reporte += (
            f"{nombre_cliente} | Pedidos: {info_cliente['cantidad_pedidos']} | "
            f"Monto: {info_cliente['monto']:.2f}\n"
        )
        reporte += info_cliente["detalles"]

    return reporte, pedidos_agrupados


def resumir_productos_vendidos(pedidos, titulo_seccion):
    """
    Resumir los productos vendidos durante el día.

    Args:
        pedidos (dict): Diccionario de pedidos.
        titulo_seccion (str): Título de la sección.

    Returns:
        tuple: (str, dict)
    """
    productos_vendidos = {}
    for id_pedido in pedidos:
        pedido = pedidos[id_pedido]
        nombre_producto = pedido["nombre_producto"]

        if nombre_producto not in productos_vendidos:
            productos_vendidos[nombre_producto] = {
                "cantidad_total": 0,
                "ventas_totales": 0.0
            }

        productos_vendidos[nombre_producto]["cantidad_total"] += pedido["cantidad"]
        productos_vendidos[nombre_producto]["ventas_totales"] += pedido["total"]

    reporte = titulo_seccion + "\n"
    reporte += "-" * len(titulo_seccion) + "\n"

    if len(productos_vendidos) == 0:
        reporte += "No se vendieron productos hoy.\n"
        return reporte, productos_vendidos

    for nombre_producto in productos_vendidos:
        info = productos_vendidos[nombre_producto]
        reporte += (
            f"{nombre_producto} | Unidades vendidas: {info['cantidad_total']} | "
            f"Monto de ventas: {info['ventas_totales']:.2f}\n"
        )

    return reporte, productos_vendidos


def generar_reporte_final(clientes, productos, pedidos, titulo_reporte):
    """
    Generar el reporte final consolidado.

    Args:
        clientes (dict): Diccionario de clientes.
        productos (dict): Diccionario de productos.
        pedidos (dict): Diccionario de pedidos.
        titulo_reporte (str): Título principal.

    Returns:
        tuple: (str, dict)
    """
    texto_pedidos, cantidad_pedidos = consultar_pedidos(pedidos, "Pedidos Registrados")
    valor_ingresos, texto_ingresos = calcular_ingresos_diarios(pedidos, "Ingresos del Día")
    texto_agrupado, datos_agrupados = agrupar_pedidos_por_cliente(pedidos, "Pedidos por Cliente")
    texto_productos, datos_productos = resumir_productos_vendidos(pedidos, "Productos Vendidos Durante el Día")
    texto_clientes, cantidad_clientes = formatear_catalogo_clientes(clientes, "Clientes Registrados")
    texto_catalogo, cantidad_productos = formatear_catalogo_productos(productos, "Productos Registrados")

    reporte = titulo_reporte + "\n"
    reporte += "=" * len(titulo_reporte) + "\n\n"
    reporte += f"Total de clientes registrados: {cantidad_clientes}\n"
    reporte += f"Total de productos registrados: {cantidad_productos}\n"
    reporte += f"Total de pedidos registrados: {cantidad_pedidos}\n"
    reporte += texto_ingresos + "\n\n"
    reporte += texto_clientes + "\n"
    reporte += texto_catalogo + "\n"
    reporte += texto_pedidos + "\n"
    reporte += texto_agrupado + "\n"
    reporte += texto_productos

    datos_reporte = {
        "total_clientes": cantidad_clientes,
        "total_productos": cantidad_productos,
        "total_pedidos": cantidad_pedidos,
        "total_ingresos": valor_ingresos,
        "pedidos_por_cliente": datos_agrupados,
        "productos_vendidos": datos_productos
    }

    return reporte, datos_reporte


def construir_texto_menu(titulo_menu, datos_opciones):
    """
    Construir el texto del menú que se muestra al usuario.

    Args:
        titulo_menu (str): Título del menú.
        datos_opciones (tuple): Opciones del menú.

    Returns:
        tuple: (str, int)
    """
    texto = "\n" + titulo_menu + "\n"
    texto += "=" * len(titulo_menu) + "\n"

    cantidad_opciones = 0
    for opcion in datos_opciones:
        texto += f"{opcion[0]}. {opcion[1]}\n"
        cantidad_opciones += 1

    return texto, cantidad_opciones


def procesar_opcion_menu(datos_sistema, opcion_seleccionada):
    """
    Ejecutar una opción del menú y retornar el estado actualizado.

    Args:
        datos_sistema (dict): Datos principales del sistema.
        opcion_seleccionada (str): Opción elegida en el menú.

    Returns:
        tuple: (dict, bool, str)
    """
    if opcion_seleccionada == "1":
        id_cliente = input("Ingrese el ID del cliente: ")
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        correo_cliente = input("Ingrese el correo del cliente: ")

        clientes_actualizados, mensaje = registrar_cliente(
            datos_sistema["clientes"], id_cliente, nombre_cliente, correo_cliente
        )
        datos_sistema["clientes"] = clientes_actualizados
        return datos_sistema, True, mensaje

    if opcion_seleccionada == "2":
        id_producto = input("Ingrese el ID del producto: ")
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_unitario = input("Ingrese el precio unitario: ")

        productos_actualizados, mensaje = registrar_producto(
            datos_sistema["productos"], id_producto, nombre_producto, precio_unitario
        )
        datos_sistema["productos"] = productos_actualizados
        return datos_sistema, True, mensaje

    if opcion_seleccionada == "3":
        id_cliente = input("Ingrese el ID del cliente: ")
        id_producto = input("Ingrese el ID del producto: ")
        cantidad = input("Ingrese la cantidad: ")

        pedidos_actualizados, contador_actualizado, mensaje = crear_pedido(
            datos_sistema["pedidos"],
            datos_sistema["clientes"],
            datos_sistema["productos"],
            datos_sistema["contador_pedidos"],
            id_cliente,
            id_producto,
            cantidad
        )
        datos_sistema["pedidos"] = pedidos_actualizados
        datos_sistema["contador_pedidos"] = contador_actualizado
        return datos_sistema, True, mensaje

    if opcion_seleccionada == "4":
        reporte, _ = consultar_pedidos(datos_sistema["pedidos"], "Pedidos Registrados")
        return datos_sistema, True, reporte

    if opcion_seleccionada == "5":
        _, mensaje = calcular_ingresos_diarios(datos_sistema["pedidos"], "Ingresos del Día")
        return datos_sistema, True, mensaje

    if opcion_seleccionada == "6":
        reporte, _ = generar_reporte_final(
            datos_sistema["clientes"],
            datos_sistema["productos"],
            datos_sistema["pedidos"],
            "Reporte Final de Ventas"
        )
        return datos_sistema, True, reporte

    if opcion_seleccionada == "7":
        return datos_sistema, False, "Programa finalizado."

    return datos_sistema, True, "Opción inválida. Inténtelo de nuevo."


def ejecutar_sistema(datos_sistema, opciones_menu):
    """
    Ejecutar el ciclo del menú en la terminal.

    Args:
        datos_sistema (dict): Datos principales del sistema.
        opciones_menu (tuple): Opciones del menú.

    Returns:
        dict: Datos finales del sistema después de la ejecución.
    """
    continuar_ejecucion = True

    while continuar_ejecucion:
        texto_menu, _ = construir_texto_menu("Sistema de Gestión de Pedidos de Clientes", opciones_menu)
        print(texto_menu)
        opcion_seleccionada = input("Seleccione una opción: ")

        datos_sistema, continuar_ejecucion, mensaje = procesar_opcion_menu(datos_sistema, opcion_seleccionada)
        print("\n" + mensaje)

    return datos_sistema


if __name__ == "__main__":
    datos_iniciales = crear_datos_sistema({}, {}, {}, 1)

    configuracion_menu = (
        ("1", "Registrar cliente"),
        ("2", "Registrar producto"),
        ("3", "Crear pedido"),
        ("4", "Consultar pedidos"),
        ("5", "Calcular ingresos del día"),
        ("6", "Generar reporte final"),
        ("7", "Salir")
    )

    ejecutar_sistema(datos_iniciales, configuracion_menu)
