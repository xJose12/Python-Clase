# Joc_02: Piedra Papel Tijeras || José Antonio Valiente Guerrero
# Importamos los modulos necesarios
import random
import os

# Limpiamos la pantalla con ayuda del modulo importado antes, ejecutando un cls 
os.system('cls')

# Definimos las funciones que se van a utilizar

# La funcion bienvenidaJuego() es la función que se encarga de mostrar la bienvenida de mi juego
def bienvenidaJuego():
    print("¡Piedra, Papel y Tijeras by Jose A!\n\nBienvenido a mi juego! \nEntra y disfruta!\nBuena Suerte!\n")
    input("Pulsa cualquier tecla para comenzar...")

# La funcion mostrarReglas() es la función que se encarga de mostrar las reglas del piedra, papel y tijeras
def mostrarReglas():
    print("¡ESTAS SON LAS REGLAS!\n- Piedra aplasta tijeras: La piedra gana contra las tijeras porque la piedra puede romper o aplastar las tijeras.\n- Tijeras cortan papel: Las tijeras ganan contra el papel porque las tijeras pueden cortar o vencer al papel.\n- Papel cubre la piedra: El papel gana contra la piedra porque el papel puede cubrir o envolver la piedra.\n")
    input("Pulsa cualquier tecla para volver al menú principal...")

# La funcion salir() es la función que se encarga de salir de mi juego
def salir():
    os.system('cls')
    print("¡Muchas gracias por jugar a mi juego, hasta la próxima!\n")

# La funcion transformarNumNombre() es la función que se encarga de transformar el número de jugada tanto de jugador como maquina al nombre que toca.
def transformarNumNombre(numero):
    jugada = {1: "Piedra", 2: "Papel", 3: "Tijeras"}
    return jugada.get(numero)

# La funcion ejecucionJuego() es la función que se encarga de realizar el juego una vez que el usuario introduzca una opción correcta.
def ejecucionJuego(eleccionJugador):
    os.system('cls')
    eleccionMaquina = random.randint(1, 3) # Se genera un número aleatorio entre 1 y 3, jugada de la maquina.

    # Se obtiene el número de la elección jugador y la elección de la maquina y se combierte con la función transformarNumNombre() para obtener el nombre de la elección jugador y maquina.
    print(f"Has elegido: {transformarNumNombre(eleccionJugador)}")
    print(f"La máquina eligió: {transformarNumNombre(eleccionMaquina)}\n")

    # Se comparan ambas elecciones y se comprueba si el número de la elección jugador es el ganador, perdedor o empate.
    if eleccionJugador == eleccionMaquina:
        print("Habéis empatado!")
    elif (eleccionJugador == 1 and eleccionMaquina == 3) or (eleccionJugador == 2 and eleccionMaquina == 1) or (eleccionJugador == 3 and eleccionMaquina == 2):
        print("¡Has ganado!")
    else:
        print("La máquina ha ganado.")

    # Se pregunta si quiere seguir jugando o no. Mediante un bucle para en caso de introducir una elección incorrecta vuelva a preguntarse.
    while True:
        seguirJugando_input = input("¿Quieres seguir jugando? (S / 'SALIR'): ").upper()

        if seguirJugando_input == "SALIR":
            salir() # Muestra el mensaje de salida del juego.
            exit() # Se cierra la ejecución del programa automático.
        elif seguirJugando_input == "S":
            return True # Devuelve True para indicar que se siga ejecutando la función menuJuego().
        else:
            os.system('cls')
            # En caso de introducir una elección incorrecta, volvera a intentarlo.
            input("Has introducido una opción incorrecta. Selecciona una opción válida...\n")

# La funcion menuJuego() es la función que se encarga de mostrar el menú del juego así como preguntar que va a jugar.
def menuJuego():
    while True: # Se utiliza un bucle para que mientras no sea lo contrario el juego se ejecute una vez y otra. De esta manera no volvemos todo el rato al menu principal.
        os.system('cls')
        print("¡Comienza el juego! ¡Mucha suerte!\n\nElige entre Piedra, Papel o Tijeras:\n- 1. Piedra\n- 2. Papel\n- 3. Tijeras\n")
        try: # Debido a que debe pasarse a tipo int ya que será un numero, se utiliza try-except para evitar errores en caso de introducir una letra.
            eleccionJugador = int(input("Tu elección es: "))
        except ValueError: 
            input("Has introducido una opción no válida. Inténtalo de nuevo...")
            continue

        # Comprobamos si el número de la elección jugador es correcto. De ser así llama a la funcion ejecucionJuego() pasando por parametro la elección jugador.
        if eleccionJugador in [1, 2, 3]:
            continuar_jugando = ejecucionJuego(eleccionJugador)
            if not continuar_jugando:
                break
        else:
            input("Has introducido una opción inválida, vuelve a intentarlo...")

# Se ejecuta la función bienvenidaJuego() para mostrar el mensaje de bienvenida.
bienvenidaJuego()

# Mostramos el menu principal. Simplemente comprueba las elecciones y se redirigen a ellas.
while True:
    os.system('cls')
    print("--- Menú de Piedra Papel Tijeras ---\n")
    print("A. Para comenzar el juego\n")
    print("B. Consultar las reglas\n ")
    print("Escribe 'SALIR' para salir del juego\n")

    opcionElegida = input("\nSelecciona una opción (A / B / SALIR): ").upper()
    os.system('cls')

    if opcionElegida == "A":
        menuJuego()
    elif opcionElegida == "B":
        mostrarReglas()
    elif opcionElegida == "SALIR":
        salir()
        break
    else:
        input("Has introducido una opción incorrecta. Selecciona una opción válida...\n")