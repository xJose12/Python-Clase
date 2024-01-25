# Joc_02: Piedra Papel Tijeras || José Antonio Valiente Guerrero
# Importamos los modulos necesarios
import random
import os

# Limpiamos la pantalla con ayuda del modulo importado antes, ejecutando un cls 
os.system('cls')

def bienvenidaJuego() :
    print("¡Piedra, Papel y Tijeras by Jose A!\n\nBienvenido a mi juego! \nEntra y disfruta!\nBuena Suerte!\n")
    input("Pulsa cualquier tecla para comenzar...")
        
def mostrarReglas() :
    print("¡ESTAS SON LAS REGLAS!\n- Piedra aplasta tijeras: La piedra gana contra las tijeras porque la piedra puede romper o aplastar las tijeras.\n- Tijeras cortan papel: Las tijeras ganan contra el papel porque las tijeras pueden cortar o vencer al papel.\n- Papel cubre la piedra: El papel gana contra la piedra porque el papel puede cubrir o envolver la piedra.\n")
    input("Pulsa cualquier tecla para volver al menu principal...")
    
def salir() :
    print("¡Muchas gracias por jugar a mi juego, hasta la proxima!\n")
        
def trasformarNumNombre(numero):
    jugada = {1: "Piedra", 2: "Papel", 3: "Tijeras"}
    return jugada.get(numero)

def menuJuego():
    while True:
        os.system('cls')
        print("¡Comienza el juego! Mucha suerte!\n\nElige entre Piedra, Papel o Tijeras:\n- 1. Piedra\n- 2. Papel\n- 3. Tijeras\n")
        try:
            eleccionJugador = int(input("Tu elección es: "))
        except ValueError:
            input("Has introducido una opción no válida. Inténtalo de nuevo...")
            continue

        if eleccionJugador in [1, 2, 3]:
            ejecucionJuego(eleccionJugador)
        else:
            input("Has introducido una opción inválida, vuelve a intentarlo...")
        
def ejecucionJuego(eleccionJugador):
    eleccionMaquina = random.randint(1,3)

    print(f"La máquina eligió: {trasformarNumNombre(eleccionMaquina)}")

    if eleccionJugador == eleccionMaquina:
        print("Habeis empatado!")
    elif (eleccionJugador == 1 and eleccionMaquina == 3) or (eleccionJugador == 2 and eleccionMaquina == 1) or (eleccionJugador == 3 and eleccionMaquina == 2):
        print("¡Has ganado!")
    else:
        print("La máquina ha ganado.")
        
    input("\nPulsa para seguir jugando...")
        
bienvenidaJuego()
    
while True:
    os.system('cls')
    print("--- Menu de Piedra Papel Tijeras ---\n")
    print("A. Para comenzar el juego\n")
    print("B. Consultar las reglas\n ")
    print("C. Salir del juego")
    
    opcionElegida = input("\nSelecciona una opcion ( A / B / C ): ")
    os.system('cls')
    
    if opcionElegida == "A" :
        menuJuego()
    elif opcionElegida == "B" :
        mostrarReglas()
    elif opcionElegida == "C" :
        salir()
        break
    else : 
        input("Has introducido una opción incorrecta. Selecciona una opcion valida...\n")