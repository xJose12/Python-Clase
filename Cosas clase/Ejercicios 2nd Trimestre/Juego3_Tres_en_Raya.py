# Joc_03: Tres en Raya || José Antonio Valiente Guerrero
# Importamos los modulos necesarios
import os

# Función para imprimir el juego de tres en raya, se le da formato y se asigna la posicion del array valores donde se introduciran X o Y. correspodiento con las 9 celdas dentro del tablero.
def imprimirTablero(valores):
    print("Tablero:\n")
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(valores[0], valores[1], valores[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(valores[3], valores[4], valores[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(valores[6], valores[7], valores[8]))
    print("\t     |     |")
    print("\n")
 
# Función para verificar si algún jugador ha ganado.
def comprobarGanador(posicionesJugador, jugadorActual):
 
    # Se almacenan las combinaciones ganadoras para posteriormente comprobar si alguna se cumple dentro del tablero.
    solucionesGanadoras = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Bucle para verificar si alguna combinación ganadora se cumple dentro del tablero. De ahí que asignemos valores a cada posicion del tablero.
    for x in solucionesGanadoras:
        if all(y in posicionesJugador[jugadorActual] for y in x):
 
            # Devuelve Verdadero si alguna combinación ganadora se cumple.
            return True
    # Devuelve Falso si ninguna combinación se cumple.
    return False       
 
# Función para verificar si el juego ha terminado en empate.
def comprobarEmpate(posicionesJugador):
    if len(posicionesJugador['X']) + len(posicionesJugador['O']) == 9:
        return True
    return False       
 
# Función de ejecución del juego
def juego(jugadorActual):
 
    # Representa el juego de tres en raya
    valores = [' ' for x in range(9)]
     
    # Almacena las posiciones ocupadas por X y O para ir comprobando en la funcion de comprobarGanador() y comprobarEmpate().
    posicionesJugador = {'X':[], 'O':[]}
     
    # Bucle del juego para una única ronda de tres en raya
    while True:
        imprimirTablero(valores)
         
        # Bloque de excepción
        try:
            print("Jugador ", jugadorActual, " turno. ¿En qué casilla? : ")
            movimiento = int(input()) 
            os.system('cls')
        except ValueError:
            print("¡Casilla incorrecta! Inténtalo de nuevo.")
            continue
 
        # Comprobación de que el valor introducido no sea menor que 1 o mayor que 9.
        if movimiento < 1 or movimiento > 9:
            print("¡Casilla incorrecta! Inténtalo de nuevo.")
            continue
 
        # Verificar si la casilla no está ocupada por otra ficha.
        if valores[movimiento-1] != ' ':
            os.system('cls')
            print("La casilla ", movimiento, " esta ocupada ¡Inténtalo de nuevo!")
            continue
 
        # Comprobadores y actualizacion del juego por cada movimiento.
 
        # Actualizando el estado del tablero.
        valores[movimiento-1] = jugadorActual
 
        # Actualizando las posiciones del jugador.
        posicionesJugador[jugadorActual].append(movimiento)
 
        # Llamar a la función para verificar si ha ganado.
        if comprobarGanador(posicionesJugador, jugadorActual):
            imprimirTablero(valores)
            print("¡El jugador ", jugadorActual, " ha ganado el juego!\n")
            return jugadorActual
 
        # Llamar a la función para verificar si el juego ha terminado en empate.
        if comprobarEmpate(posicionesJugador):
            imprimirTablero(valores)
            print("Empate\n")
            return 'D'
 
        # Cambio de jugador.
        if jugadorActual == 'X':
            jugadorActual = 'O'
        else:
            jugadorActual = 'X'
 
os.system('cls')
print("¡Tres en raya by Jose A!\n\nBienvenido a mi juego! \nEntra y disfruta! Buena Suerte!\n")
print("Recuerda: Para seleccionar una elección dentro del tablero, debe introducir la posición de la casilla en la que deseas poner tu ficha. Del 1 al 9 respectivamente.\n")
input("Pulsa cualquier tecla para comenzar...")
os.system('cls')

print("Jugador 1")
jugador1 = input("Ingresa el nombre: ")
print("\n")
 
print("Jugador 2")
jugador2 = input("Ingresa el nombre: ")
print("\n")
os.system('cls')
     
# Almacena el jugador que elige X y O
jugadorActual = jugador1

# Almacena la elección de los jugadores
eleccionJugador = {'X' : "", 'O' : ""}
 
# Almacena las opciones
opciones = ['X', 'O']
 
# El bucle se ejecuta hasta que los jugadores decidan salir
while True:
 
    # Menú de elección del jugador
    print("Turno del jugador", jugadorActual, "\nElige tu ficha en el tablero:")
    print("Pulsa '1' para X")
    print("Pulsa '2' para O")
    print("Pulsa '3' para Salir")
 
    # Bloque de excepción para la entrada de ELECCIÓN
    try:
        eleccion = int(input())
        os.system('cls')
    except ValueError:
        print("¡Entrada incorrecta! Inténtalo de nuevo\n")
        continue
 
    # Condiciones para la elección del jugador
    if eleccion == 1:
        eleccionJugador['X'] = jugadorActual
        if jugadorActual == jugador1:
            eleccionJugador['O'] = jugador2
        else:
            eleccionJugador['O'] = jugador1
 
    elif eleccion == 2:
        eleccionJugador['O'] = jugadorActual
        if jugadorActual == jugador1:
            eleccionJugador['X'] = jugador2
        else:
            eleccionJugador['X'] = jugador1
         
    elif eleccion == 3:
        print("Muchas gracias por participar en el juego!\n")
        break  
 
    else:
        print("¡Elección incorrecta! Inténtalo de nuevo\n")
 
    # Almacena el ganador
    ganador = juego(opciones[eleccion-1])
    
    # Cambio de jugador por si quieren seguir jugando, para que empiece el otro
    if jugadorActual == jugador1:
        jugadorActual = jugador2
    else:
        jugadorActual = jugador1