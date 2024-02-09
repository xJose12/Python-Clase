# Script para Crear Usuarios en Debian.
# José Antonio Valiente Guerrero

# Importamos las librerias que necesitamos.
import subprocess # Se utiliza para ejectuar comandos del sistema.
import sys # Se utiliza para la salida en caso de error, en este script.
import getpass # Utilizado para obtener la contraseñas de forma segura.

# Crearemos una función para hacerlo todo que posteriormente llamaremos.
def adduser():
    # Crearemos una variable para almacenar el nombre de usuario, nombre completo y la contraseña.
    usuario = input("Introduce el nombre de Usuario que quieras crear: ")
    nombreCompleto = input("Introduce el nombre completo del Usuario: ")
    password = getpass.getpass("Introduce la contraseña del Usuario:") # Getpass transforma el texto plano a una contraseña segura, que entienda el sistema.
    askAdministrator = input(f"¿Quieres que tu usuario {usuario} sea administrador? (S/N): ").lower() # Pregunta si quieremos que nuestro usuario sea administrador S/N.
    # Almacena el resultado en una variable admin para saber que ha elegido el usuario.
    if askAdministrator == "s":
        admin = True
    elif askAdministrator == "n":
        admin = False
    else:
        print("Opcion Invalida")
        sys.exit(1)

    try: # Comprobamos los pasos para crear el usuario con ckeck=True por si ya existe el usuario o falla algo que nos muestre el error y devuelva un codigo de salida en valor 1.
        crearUsuario = ['sudo', 'useradd', '-m', '-s', '/bin/bash', usuario] # Almacenamos todos los parametros en una lista, -m indica que se crea un directorio de inicio para este usuario y -s establece el shell del nuevo usuario para que podamos usar el terminal sin problema, de esta manera nos podremos loggear sin ni siquiera iniciar sesion por primera vez en la interfaz de loggin.
        # Agregaremos la condición de -G sudo si el usuario será administrador, con sudo automaticamente pasa a ser admin.
        if admin:
            crearUsuario += ['-G', 'sudo']
        # usamos .run para ejecutar los comandos pasandole la lista.
        subprocess.run(crearUsuario, check=True)
        
        subprocess.run(['sudo', 'chfn', '-f', nombreCompleto, usuario], check=True) # chfn se utiliza para cambiar la información de un usuario con -f especificamos el nombre complet del usuario y se cambia.

        # Utilizamos .Popen para crear un nuevo proceso donde ejecutara el cambio de la contraseña, indicandole que vamos a reedirigir mediante un PIPE este proceso hijo siendo "stdin", de ahí que abajo introduzcamos la contraseña 2 veces.
        p = subprocess.Popen(['sudo', 'passwd', usuario], stdin=subprocess.PIPE)
        p.communicate(f"{password}\n{password}\n".encode()) # Con el PIPE activo, enviamos 2 veces la contraseña, esto es por la confirmacion de Volver a Introducir Contraseña.

        print(f"Usuario '{usuario}' agregado con éxito y contraseña establecida.") # Feedback en caso de que se cree todo correcto.
        
    except: # En caso de que algo de error o falle, se nos imprime un mensaje de error al crear y sale el programa, con el codigo de error. De ahí el usar sys.exit.
        print(f"Error al crear el usuario: {usuario}")
        sys.exit(1)

# Ejecucion de la funcion de crear usuario en Debian.
adduser()