import hashlib
import getpass
import platform
import subprocess

def codificar_dato(dato:str):
    return hashlib.sha256(dato.encode('utf-8')).hexdigest()

def limpiar_consola() -> None:
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)
        subprocess.run("clear", shell=True)

def ingresar_cadena(mensaje:str,mensaje_error:str,minimo_caracteres:int) -> str:
    cadena = input(mensaje)

    while len(cadena) < minimo_caracteres:
        print(mensaje_error)
        cadena = input(mensaje)
    
    return cadena

def ingresar_dato_sensible(mensaje:str,mensaje_error:str,minimo_caracteres:int) -> str:
    dato_sensible = getpass.getpass(mensaje)

    while len(dato_sensible) < minimo_caracteres:
        print(mensaje_error)
        dato_sensible = getpass.getpass(mensaje) 

    return dato_sensible

def verificar_usuario(lista_usuarios:list,nombre_usuario:str,clave_hash:str) -> bool:
    for i in range(len(lista_usuarios)):
        if nombre_usuario == lista_usuarios[i].get("nombre_usuario") and clave_hash == lista_usuarios[i].get("clave"):
            return True
        
    return False
    
def buscar_usuario(lista_usuarios:list,nombre_usuario:str) -> dict | None:
    for i in range(len(lista_usuarios)):
        if nombre_usuario == lista_usuarios[i].get("nombre_usuario"):
            return lista_usuarios[i]
        
    return None

def iniciar_sesion(lista_usuarios:list,caracteres_usuario:int,caracteres_clave:int,mensaje_error:str = "credenciales incorrectas",cantidad_intentos:int = 3) -> dict | None:
    intentos = 0
    nombre_usuario = ingresar_cadena("Ingrese el nombre de usuario: ",f"La cadena debe tener al menos {caracteres_usuario} caracteres",caracteres_usuario)
    clave = ingresar_dato_sensible("Ingrese la contraseña: ",f"La contraseña debe tener al menos {caracteres_clave} caracteres",caracteres_clave)
    clave_hash = codificar_dato(clave)

    while verificar_usuario(lista_usuarios,nombre_usuario,clave_hash) == False:
        limpiar_consola()
        intentos += 1 
        if intentos == cantidad_intentos:
            limpiar_consola()
            print("Se quedo sin intentos")
            return None
        
        print(mensaje_error)
        nombre_usuario = ingresar_cadena("Ingrese el nombre de usuario: ",f"La cadena debe tener al menos {caracteres_usuario} caracteres",caracteres_usuario)
        clave = ingresar_dato_sensible("Ingrese la contraseña: ",f"La contraseña debe tener al menos {caracteres_clave} caracteres",caracteres_clave)
        clave_hash = codificar_dato(clave)

    usuario_encontrado = buscar_usuario(lista_usuarios,nombre_usuario)
    return usuario_encontrado