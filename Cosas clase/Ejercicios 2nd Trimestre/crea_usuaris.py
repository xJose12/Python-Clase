import subprocess
import sys
import getpass
 
def add_user():
 
    username = input("Introduce el nombre de Usuario que quieras crear: ")   

    password = getpass.getpass("Introduce la contraseña del Usuario:")
        
    try:
        subprocess.run(['useradd', username])
        
        p = subprocess.Popen(['chpasswd'], stdin=subprocess.PIPE)
        p.communicate(f"{username}:{password}".encode())
        
        print(f"Usuario '{username}' agregado con exito.")
    except:
        print(f"Error al crear el usuario.")                     
        sys.exit(1)
 
add_user()