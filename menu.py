"""Módulo de menús y control de navegación del sistema."""

from login import iniciar_sesion
from entradas import ingresar_entero_positivo
from funciones import (
    leer_json,
    ordenar_transferencias_burbuja,
    buscar_usuario_por_cbu_o_alias,
    realizar_transferencia,
)
from salidas import (
    formatear_monto,
    mostrar_datos_personales,
    mostrar_historial_transferencias,
    mostrar_todas_las_transferencias,
    mostrar_mensaje_salida,
)


def transferir_dinero(usuario, lista_usuarios, lista_transferencias):
    """Pide destino y monto, y ejecuta la transferencia."""
    dato = input("CBU o alias del destinatario: ")
    destino = buscar_usuario_por_cbu_o_alias(lista_usuarios, dato)
    monto = ingresar_entero_positivo(
        "Monto a transferir: ", "Ingresá solo números positivos."
    )
    ok, mensaje = realizar_transferencia(
        usuario, destino, monto, lista_usuarios, lista_transferencias
    )
    print(mensaje)


def ejecutar_menu_cliente(usuario, lista_usuarios, lista_transferencias):
    """Menú interactivo para usuarios con rol cliente."""
    activo = True
    while activo:
        print("\n========================================")
        print(
            "BIENVENIDO:",
            usuario["nombre"],
            usuario["apellido"],
            "| SALDO:",
            formatear_monto(usuario["saldo"]),
        )
        print("========================================")
        print("1. Ver datos personales")
        print("2. Transferir dinero")
        print("3. Ver historial de transferencias")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_datos_personales(usuario)
        elif opcion == "2":
            transferir_dinero(usuario, lista_usuarios, lista_transferencias)
        elif opcion == "3":
            mostrar_historial_transferencias(lista_transferencias, usuario["cbu"])
        elif opcion == "4":
            mostrar_mensaje_salida()
            activo = False
        else:
            print("Opción inválida.")


def ejecutar_menu_administrador(usuario, lista_usuarios, lista_transferencias):
    """Menú básico para el administrador (ampliar según el TP)."""
    activo = True
    while activo:
        print("\n--- ADMINISTRADOR:", usuario["nombre_usuario"], "---")
        print("1. Ver todas las transferencias (de mayor a menor)")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ordenadas = ordenar_transferencias_burbuja(lista_transferencias)
            mostrar_todas_las_transferencias(ordenadas)
        elif opcion == "2":
            mostrar_mensaje_salida()
            activo = False
        else:
            print("Opción inválida.")


def gestionar_billetera():
    """Carga archivos, ejecuta el login y redirige al menú correspondiente."""
    lista_usuarios = leer_json("usuarios.json")
    lista_transferencias = leer_json("transferencias.json")

    usuario_logueado = iniciar_sesion(
        lista_usuarios,
        caracteres_usuario=6,
        caracteres_clave=6,
        mensaje_error="Credenciales incorrectas",
        cantidad_intentos=3,
    )

    if usuario_logueado is None:
        print("Se quedó sin intentos. Programa finalizado por seguridad.")
    elif usuario_logueado["rol"] == "cliente":
        ejecutar_menu_cliente(usuario_logueado, lista_usuarios, lista_transferencias)
    elif usuario_logueado["rol"] == "administrador":
        ejecutar_menu_administrador(
            usuario_logueado, lista_usuarios, lista_transferencias
        )
