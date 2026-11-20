"""Módulo de lógica de negocio, manejo de JSON y algoritmos propios."""

import json
from datetime import datetime


def leer_json(nombre_archivo):
    """Lee un archivo JSON y devuelve su contenido. Devuelve [] si no existe."""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar_json(nombre_archivo, datos):
    """Guarda los datos en un archivo JSON."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def calcular_edad(fecha_nacimiento):
    """Calcula la edad a partir de una fecha DD-MM-YYYY."""
    dia = int(fecha_nacimiento[0:2])
    mes = int(fecha_nacimiento[3:5])
    anio = int(fecha_nacimiento[6:10])

    hoy = datetime.now()
    edad = hoy.year - anio
    if (hoy.month, hoy.day) < (mes, dia):
        edad = edad - 1
    return edad


def fecha_actual():
    """Devuelve la fecha de hoy en formato DD-MM-YYYY."""
    return datetime.now().strftime("%d-%m-%Y")


def sumar_montos(lista_montos):
    """Suma una lista de montos sin usar sum()."""
    acumulador = 0.0
    i = 0
    while i < len(lista_montos):
        acumulador = acumulador + float(lista_montos[i])
        i = i + 1
    return acumulador


def obtener_maximo_monto(lista_montos):
    """Obtiene el monto máximo sin usar max()."""
    if len(lista_montos) == 0:
        return 0.0
    maximo = float(lista_montos[0])
    i = 1
    while i < len(lista_montos):
        if float(lista_montos[i]) > maximo:
            maximo = float(lista_montos[i])
        i = i + 1
    return maximo


def obtener_minimo_monto(lista_montos):
    """Obtiene el monto mínimo sin usar min()."""
    if len(lista_montos) == 0:
        return 0.0
    minimo = float(lista_montos[0])
    i = 1
    while i < len(lista_montos):
        if float(lista_montos[i]) < minimo:
            minimo = float(lista_montos[i])
        i = i + 1
    return minimo


def ordenar_transferencias_burbuja(lista_transferencias):
    """Devuelve una COPIA ordenada de mayor a menor monto (burbuja)."""
    lista = []
    k = 0
    while k < len(lista_transferencias):
        lista.append(lista_transferencias[k])
        k = k + 1

    largo = len(lista)
    i = 0
    while i < largo - 1:
        j = 0
        while j < largo - 1 - i:
            if float(lista[j]["monto"]) < float(lista[j + 1]["monto"]):
                auxiliar = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = auxiliar
            j = j + 1
        i = i + 1
    return lista


def buscar_usuario_por_cbu_o_alias(lista_usuarios, dato):
    """Busca un usuario por CBU o alias. Devuelve None si no existe."""
    i = 0
    while i < len(lista_usuarios):
        u = lista_usuarios[i]
        if u ["cbu"] == dato or u["alias"] == dato:
            return u
        i = i + 1
    return None


def realizar_transferencia(
    origen, destino, monto, lista_usuarios, lista_transferencias
):
    """Valida y ejecuta una transferencia. Devuelve (ok, mensaje)."""
    if destino is None:
        return False, "El destinatario no existe."
    if destino["cbu"] == origen["cbu"]:
        return False, "No podés transferirte a vos mismo."
    if monto <= 0:
        return False, "El monto debe ser mayor a cero."
    if monto > float(origen["saldo"]):
        return False, "Saldo insuficiente."

    origen["saldo"] = float(origen["saldo"]) - monto
    destino["saldo"] = float(destino["saldo"]) + monto
    lista_transferencias.append(
        {
            "fecha": fecha_actual(),
            "cbu_origen": origen["cbu"],
            "cbu_destino": destino["cbu"],
            "monto": monto,
        }
    )
    guardar_json("usuarios.json", lista_usuarios)
    guardar_json("transferencias.json", lista_transferencias)
    return True, "Transferencia realizada con éxito."
