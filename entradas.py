"""Módulo de entradas y validaciones manuales sin métodos de string prohibidos."""


def es_digito(cadena):
    """Valida manualmente si una cadena contiene solo dígitos numéricos."""
    if len(cadena) == 0:
        return False
    i = 0
    while i < len(cadena):
        if cadena[i] < "0" or cadena[i] > "9":
            return False
        i = i + 1
    return True


def es_alfabetico_con_espacios(cadena):
    """Valida letras, espacios y la ñ."""
    if len(cadena) == 0:
        return False
    i = 0
    while i < len(cadena):
        c = cadena[i]
        es_letra = (
            (c >= "a" and c <= "z")
            or (c >= "A" and c <= "Z")
            or c == "ñ"
            or c == "Ñ"
            or c == " "
        )
        if not es_letra:
            return False
        i = i + 1
    return True


def ingresar_cadena_longitud(mensaje, mensaje_error, min_caracteres, max_caracteres):
    """Pide una cadena asegurando un rango de longitud."""
    texto = input(mensaje)
    while len(texto) < min_caracteres or len(texto) > max_caracteres:
        print(mensaje_error)
        texto = input(mensaje)
    return texto


def ingresar_entero_positivo(mensaje, mensaje_error):
    """Pide un entero validando que no tenga letras ni signo negativo."""
    entrada = input(mensaje)
    while not es_digito(entrada):
        print(mensaje_error)
        entrada = input(mensaje)
    return int(entrada)
