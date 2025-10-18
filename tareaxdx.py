# importar biblioteccas para guardar datos
import json  
import os 
from login import iniciar_sesion, registrar_usuario
#definiendo lista global
transacciones = []
#definir funcion para cargar los datos
def cargarD():
    global transacciones 
    if os.path.exists("gastos_familiares.json"): 
        with open("gastos_familiares.json", "r") as archivo:
            transacciones = json.load(archivo) 
    else:
        pass
#definir funcion para que el usuario ingrese datos
def agregarIng():
    try:
        cantidad = float(input("Ingresa la cantidad del ingreso: $"))
        descripcion = input("Ingresa una descripción para el ingreso: ")
        transaccion = {
            "tipo": "ingreso",
            "cantidad": cantidad, #definir un  diccionario transaccion para guardar los datos que se ingresen 
            "descripcion": descripcion
        }
        transacciones.append(transaccion)
        print(f" Ingreso de ${cantidad:.2f} añadido correctamente")
    except ValueError:
        print(" Por favor, ingresa una cantidad numérica válida")
#definir funcion para agregar gastos
def agregar_gasto():
    print("\n--- Categorías de Gastos ---") 
    categorias = ["Alimentos", "Transporte", "Vivienda", "Entretenimiento", "Otros"]
    for i, cat in enumerate(categorias, 1): #enumerate recorre todo el diccionario de categorias
        print(f"{i}. {cat}")
    
    try: 
        opcion_cat = int(input("Elige una categoría (número): "))
        if 1 <= opcion_cat <= len(categorias):
            categoria_elegida = categorias[opcion_cat - 1]
            cantidad = float(input(f"Ingresa la cantidad del gasto para '{categoria_elegida}': $"))
            descripcion = input("Ingresa una descripción para el gasto: ")
            
            transaccion = {
                "tipo": "gasto",
                "cantidad": cantidad,
                "descripcion": descripcion,
                "categoria": categoria_elegida
            }
            transacciones.append(transaccion) #añadiendo el diccionario a la lista global
            print(f" Gasto de ${cantidad:.2f} en '{categoria_elegida}' añadido")
        else:
            print(" Opción de categoría no válida")
    except (ValueError, IndexError): #usando exceps para manejar errores
        print(" Entrada no válida. Asegúrate de ingresar un gasto real")

def mostrarR():    #creando funcion para mostrar y calcular el balance final
    ingresosT = 0.0
    gastosDC = {
        "Alimentos": 0.0,
        "Transporte": 0.0,
        "Vivienda": 0.0,
        "Entretenimiento": 0.0,
        "Otros": 0.0
    }                                    

    for t in transacciones:
        if t["tipo"] == "ingreso":
            ingresosT += t["cantidad"]
        elif t["tipo"] == "gasto":
            categoria = t["categoria"]
            gastosDC[categoria] += t["cantidad"]

    gastos_totales = sum(gastosDC.values())  #Se calcula el balance
    
    print("\n--- Resumen de Gastos ---")
    for categoria, total in gastosDC.items():
        if total > 0:
            print(f"- {categoria}: ${total:.2f}")
    balance = ingresosT - gastos_totales
    print("\n--- Balance Total ---")
    print(f" Ingresos Totales: ${ingresosT:.2f}")
    print(f" Gastos Totales: ${gastos_totales:.2f}")
    print(f" Balance Final: ${balance:.2f}")
    
    if balance > 0:
        print("Felicitaciones. Estás gestionando bien tu dinero")
    elif balance < 0:
        print("Cuidado. Tus gastos superan a tus ingresos")
    else:
        print("Tus ingresos y gastos están equilibrados ")

def menu(): #funcion principal que hace funcionar a todo el programa
    cargarD()
    usuario_logueado = False
    while not usuario_logueado: #haciendo menu para el login
        print("FinZen")
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcionLogin = input("Elige una opción: ")
    
        if opcionLogin == "1":
            if iniciar_sesion():
                usuario_logueado = True
            else:
                print("No se pudo inicar sesion. vuelve a intentarlo")
        elif opcionLogin == "2":
            registrar_usuario()
            print("\n  Volviendo...")
        elif opcionLogin == "3":
            print("saliendo del programa")
            return
        else:
            print("Opcion no valida. elige correctamente")
        if usuario_logueado:
            while True:
                print("\n=== MENÚ PRINCIPAL ===")
                print("1. Agregar un nuevo ingreso")
                print("2. Agregar un nuevo gasto") #una vez logueado se manda el menu principal
                print("3. Ver resumen y balance")
                print("4. Salir del programa")
        
                opcion = input("Elige una opción (1-4): ")
        
                if opcion == "1":
                    agregarIng() 
                elif opcion == "2":
                    agregar_gasto()
                elif opcion == "3":               #se usan if elif y else para ejecutar la funcion que se elija
                    mostrarR()
                elif opcion == "4":
                    guardarD()
                    print("Saliendo...")
                    break
                else:
                    print("Opción no válida. Por favor, elige un número del 1 al 4")

# fucnion para guardar los datos
def guardarD():
    with open("gastos_familiares.json", "w") as archivo:
        json.dump(transacciones, archivo, indent=4)

if __name__ == "__main__":
    menu() #se ejecuta el script
