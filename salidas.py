"""Módulo de salidas y visualización de información para la Billetera Virtual."""

from funciones import (
    calcular_edad,
    sumar_montos,
    obtener_maximo_monto,
    obtener_minimo_monto,
)


def formatear_monto(monto):
    """Devuelve el monto como texto con 2 decimales. Ej: $1500.00"""
    return "$" + f"{float(monto):.2f}"


def mostrar_datos_personales(usuario):
    """Muestra todos los datos del cliente logueado, excepto su clave."""
    print("\n========================================")
    print("         TUS DATOS PERSONALES           ")
    print("========================================")
    print("Nombre de usuario:", usuario["nombre_usuario"])
    print("Nombre:", usuario["nombre"])
    print("Apellido:", usuario["apellido"])
    print("DNI:", usuario["dni"])
    print("CBU:", usuario["cbu"])
    print("Alias:", usuario["alias"])
    print("Saldo actual:", formatear_monto(usuario["saldo"]))

    # Edad calculada a partir de la fecha de nacimiento
    edad = calcular_edad(usuario["fecha_nacimiento"])
    print("Edad:", edad, "años")
    print("========================================")


def mostrar_transferencia(t):
    """Muestra el detalle de una transferencia en una línea."""
    print(
        "Fecha:", t["fecha"],
        "| Origen:", t["cbu_origen"],
        "| Destino:", t["cbu_destino"],
        "| Monto:", formatear_monto(t["monto"]),
    )


def mostrar_historial_transferencias(lista_transferencias, cbu_usuario):
    """Muestra las transferencias en las que participó el usuario
    (como origen o destino) junto con sus estadísticas.
    """
    print("\n========================================")
    print("      HISTORIAL DE TRANSFERENCIAS       ")
    print("========================================")

    montos_participados = []
    i = 0
    while i < len(lista_transferencias):
        t = lista_transferencias[i]
        if t["cbu_origen"] == cbu_usuario or t["cbu_destino"] == cbu_usuario:
            mostrar_transferencia(t)
            montos_participados.append(float(t["monto"]))
        i = i + 1

    print("----------------------------------------")
    if len(montos_participados) == 0:
        print("No registraste transferencias en el sistema.")
    else:
        # Estadísticas con funciones propias (sin sum, max, min)
        total = sumar_montos(montos_participados)
        monto_alto = obtener_maximo_monto(montos_participados)
        monto_bajo = obtener_minimo_monto(montos_participados)
        promedio = total / len(montos_participados)

        print("ESTADÍSTICAS DE TUS MOVIMIENTOS:")
        print("• Monto total transferido:", formatear_monto(total))
        print("• Transferencia más alta:", formatear_monto(monto_alto))
        print("• Transferencia más baja:", formatear_monto(monto_bajo))
        print("• Monto promedio por transferencia:", formatear_monto(promedio))
    print("========================================")


def mostrar_todas_las_transferencias(lista_ordenada):
    """Para el administrador: muestra todas las transferencias recibidas."""
    print("\n========================================")
    print("  TODAS LAS TRANSFERENCIAS (MAYOR A MENOR) ")
    print("========================================")
    if len(lista_ordenada) == 0:
        print("No hay transferencias registradas.")
    i = 0
    while i < len(lista_ordenada):
        mostrar_transferencia(lista_ordenada[i])
        i = i + 1
    print("========================================")


def mostrar_mensaje_salida():
    """Muestra un mensaje de despedida al salir de la aplicación."""
    print("\nGracias por utilizar WalletUTN. ¡Hasta luego!")
