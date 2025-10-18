import os
import json

archivos_usuarios = "usuarios.json"

def cargar_usuarios():
    if os.path.exists(archivos_usuarios):
        with open(archivos_usuarios, "r") as archivo:
            return json.load(archivo)
        return json.load(archivo)
    return{}

def registrar_usuario():
    usuarios = cargar_usuarios()
    print("\n ---REGISTRO---")
    usuario = input("Ingrese un correo electronico: ")
    if usuario in usuarios:
        print("Ese correo ya ha sido ingresado. Intentalo de nuevo")
        return False
    contraseña = input("Ingrese una contraseña: ")
    confirmar = input("Confirma tu contraseña: ")
    if contraseña != confirmar:
        print("Las contraseñas no coinciden")
        return False
    usuarios[usuario] = contraseña
    guardar_usuarios(usuarios)
    print("usuario registrado con exito ahora inicia sesion \n")
    return True

def iniciar_sesion():
    usuarios = cargar_usuarios()
    print("\n ---INICIO DE SESION---")
    usuario = input("ingresa tu correo: ")
    contraseña = input("ingresa tu contraseña: ")
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print(f"Bienvenido a FinZen, {usuario}\n")
        return  True
    else:
        print("Usuario o contraseña incorrectos \n")
        return False

def guardar_usuarios(usuarios):
    with open(archivos_usuarios, "w") as archivo:
        json.dump(usuarios, archivo, indent=4)