# Establecer variables/array e importar modulos
import os
alumnos = {}

# Limpiamos la pantalla ejecutando por consola un cls
os.system('cls')

# FUNCIONES

# La funcion pausarContinuar simplemente es para dar mas inmersión al usuario y limparle la pantalla despues de presionar enter, y que no se muestre el menu todo el rato y sea confusivo o molesto.
def pausarContinuar() :
    continuar = input("\nPulsa cualquier tecla para continuar...")
    os.system('cls')

# La funcion consultarRegistro a partir de un input mira si existe en la array alumnos y en caso de que si coge el nombre y el value siendo la edad.
def consultarRegistro() :
    print("Has seleccionado la opción 'A': Consultar Registros.")
    key = input("\nIntroduce el nombre del registro que quieres consultar: ")
    if key in alumnos:
        print(f"\nEl alumno {key} tiene {alumnos[key]} años.")
    else:
        print(f"\nEl alumno {key} no se encuentra en el diccionario.")
    pausarContinuar()

# La funcion insertarValores va añadiendo nuevas entradas a la array alumnos siendo la key el nombre + apellido junto estableciendo su valor que será la edad. Posteriormente se muestra por pantalla. 
def insertarValores() :
    print("Has seleccionado la opción 'B': Insertar Valores.")
    key = input("\nIntroduce la primera letra del nombre y el 1r apellido: ")
    value = int(input("Ingresa tu edad: "))
    alumnos[key] = value
    print(f"Se ha añadido el registro {key} con la edad {value}.")
    pausarContinuar()

# La funcion mostrarDiccionario recorre todos los items de la array alumnos siendo key y value los que extrae y posteriormente los imprime por pantalla. 
def mostrarDiccionario() :
    print("Has seleccionado la opción 'C': Mostrar Diccionario.")
    print("\nAquí tienes todo el diccionario completo de alumnos: ")
    for key, value in alumnos.items():
        print(f"{key}: {value} años")
    pausarContinuar()

# Se muestra el menu y como siempre es true de momento, siempre se mostrará cada vez que hagamos cualquier cosa, excepto salir del programa que lo para. 
while True:
    print("--- Menu de Consultas de Nombres y Edades ---")
    print("\nA. Consultar registros a partir de un 'username' ")
    print("B. Insertar un nuevo registro ")
    print("C. Mostrar el diccionario completo ")
    print("D. Salir del programa. ")
    
    # Se escoge una opción con un input.
    opcionElegida = input("\nSelecciona una opcion ( A / B / C / D ): ")
    os.system('cls')
    
    # Con un if mirando la opción se redirige a la funcion requerida.
    if opcionElegida == "A" :
        consultarRegistro()
    elif opcionElegida == "B" :
        insertarValores()
    elif opcionElegida == "C" :
        mostrarDiccionario()
    elif opcionElegida == "D" :
        # Se utiliza break para salir y parar de ejecutar el programa.
        print("Cerrando menu, gracias por utilizarme.")
        break
    else : 
        # En caso de introducir un valor que no este dentro de los que queremos del if, se mostrará un mensaje de error informativo.
        print("Has introducido una opción incorrecta. Selecciona una opcion valida.\n")