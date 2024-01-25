# Joc_01: Endevina el número secret || José Antonio Valiente Guerrero
# Importamos los modulos necesario
import os
import random

# Limpiamos la pantalla con ayuda del modulo importado antes, ejecutando un cls 
os.system('cls')

# Establecemos y asignamos las variables que vamos a usar
# Primero, generamos un numero random entre 2 valores con ayuda del modulo random adjuntando la funcion randint.
num_aleatorio = random.randint(1,10)
# Iniciamos el contador a 0 de intentos
num_intentos = 0

# Mensaje de bienvenida al juego
print("¡ADIVINA EL NUMERO by Jose A!\n")

print("Bienvenido a mi juego! \n")
print("A continuación deberás introducir un numero entre 1 y 10 para lograr adivinar el numero aleatorio\nBuena Suerte!\n")
input("Pulsa cualquier tecla para comenzar...")
os.system('cls') # Limpiamos pantalla

# Iniciamos un bucle que mientras adivinar no sea igual a num_aleatorio se ejecutará
while True:
    # Solicitamos al usuario que ingrese un numero para que se compruebe y lo almacenamos en una variable
    adivinar = int(input("Dime el numero a acertar: "))
    os.system('cls') # Limpiamos pantalla
    num_intentos += 1 # Incrementamos el numero de intentos ya que ha fallado.
    
    #Comprobamos primero si el numero introducido es el igual al aleatorio, si es igual te da la enhorabuena y sale del bucle, sino sigue.
    if (adivinar == num_aleatorio):
        print("El numero era el " + str(adivinar) + " , lo has adivinado con " + str(num_intentos) + " intentos! Enhorabuena!!\n")
        break
    else:
        # Mostramos un feedback al usuario junto con una pista
        print("Lo siento ese no era el numero :(")
        print("Llevas " + str(num_intentos) + " intentos" )
        print("Te voy a dar una pista:", end=" ")
        if (adivinar > num_aleatorio): # Se compara si el numero introducido es mayor que el numero random y se dice que es mas pequeño, sino mas grande.
            print("Es mas pequeño!\n")
        else:
            print("Es mas grande!\n") 