# Jose Antonio Valiente Guerrero
# Importamos las librerias que vamos a usar
import csv
import paramiko
    
# Estableceremos una funciona para sacar la informacion, otra para crear el csv y otra para crear el html.
def sacarInformacion (ip, port, username, password):
    # Basicamente se conecta por ssh con los parametros pasados y ejecuta comandos de linux para sacar la informacion y almacenarla en variables diferentes.
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ip, port, username, password)
    stdin, ipv4_maquina, stderr = ssh_client.exec_command(r"ip addr | grep -Eo 'inet ([0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}' | grep -v 127.0.0.1 | awk '{print $2}'")
    stdin, hostname_maquina, stderr = ssh_client.exec_command(r"hostname")
    stdin, MAC_maquina, stderr = ssh_client.exec_command(r"ip addr | grep -Eo 'link/ether [^ ]+' | awk '{print $2}'")
    stdin, procesador_maquina, stderr = ssh_client.exec_command(r"lshw | grep -A 4 '*-cpu' | grep 'producto:' | awk '{print $2}'")
    stdin, modeloprocesador_maquina, stderr = ssh_client.exec_command(r"lshw | grep -A 4 '*-cpu' | grep 'producto:' | awk '{print $3, $4, $5, $6, $7}'")
    stdin, frecuenciaMicro_maquina, stderr = ssh_client.exec_command(r"lscpu | grep 'CPU MHz' | awk '{print $3}'")
    stdin, numeroNucleos_maquina, stderr = ssh_client.exec_command(r"lscpu | grep '^CPU(s):' | awk '{print $2}'")
    stdin, ramCantidad_maquina, stderr = ssh_client.exec_command(r"free -h | grep Mem | awk '{print $2}'")
    stdin, porcentajeRamLibre_maquina, stderr = ssh_client.exec_command(r"free | grep Mem | awk '{print ($4/$2) * 100}'")
    stdin, comprobarRoot_maquina, stderr = ssh_client.exec_command(r"grep -c 'root:x:0' /etc/passwd")
    stdin, puertoSSH_maquina, stderr = ssh_client.exec_command(r"ss -tuln | grep ':22' | wc -l")
    stdin, puertoHTTP_maquina, stderr = ssh_client.exec_command(r"ss -tuln | grep ':80' | wc -l")
    stdin, puertoSMTP_IMAP_maquina, stderr = ssh_client.exec_command(r"ss -tuln | grep -E ':25 |:143' | wc -l")
    comandoLogon = r"last -1 | awk 'NR==1 {print $7" + '"-"' + "$4" + '"-"' + "$6" + '"-"' + "$5}'"
    stdin, ultimoLogon_maquina, stderr = ssh_client.exec_command(comandoLogon)

    # Cambio el 1 o 2 de los comprobar los puertos o si es root por True or False
    comprobarRoot_maquina = [True if int(line.strip()) == 1 else False for line in comprobarRoot_maquina]
    puertoSSH_maquina = [True if int(line.strip()) == 2 else False for line in puertoSSH_maquina]
    puertoHTTP_maquina = [True if int(line.strip()) == 1 else False for line in puertoHTTP_maquina]
    puertoSMTP_IMAP_maquina = [True if int(line.strip()) == 1 else False for line in puertoSMTP_IMAP_maquina]

    # Almaceno todos los datos en un lista
    datos = {
        "IP": [line.strip() for line in ipv4_maquina],
        "Hostname": [line.strip() for line in hostname_maquina],
        "MAC": [line.strip() for line in MAC_maquina],
        "Nombre Usuario": [username],
        "Nombre Procesador": [line.strip() for line in procesador_maquina],
        "Modelo Procesador": [line.strip() for line in modeloprocesador_maquina],
        "Frecuencia Procesador": [line.strip() for line in frecuenciaMicro_maquina],
        "Numero Nucleos": [line.strip() for line in numeroNucleos_maquina],
        "Cantidad RAM": [line.strip() for line in ramCantidad_maquina],
        "% RAM libre": [line.strip() for line in porcentajeRamLibre_maquina],
        "Comprobar Root": comprobarRoot_maquina,
        "Puerto SSH": puertoSSH_maquina,
        "Puerto HTTP": puertoHTTP_maquina,
        "Puerto SMTP - IMAP": puertoSMTP_IMAP_maquina,
        "Ultimo Logon": [line.strip() for line in ultimoLogon_maquina]        
    }
    # Saco el valor maximo de la lista para poner un tope a los bucles que escriben
    maxDatos = max(len(datos[key]) for key in datos)
    ssh_client.close()
    # Devuelvo los 2 valores para que se creen el CSV, HTML o ambos segun elija el usuario
    return datos, maxDatos

def crearCSV(datos, maxDatos):
    # Creamos un archivo csv y almacenamos los datos de cada columna.
    with open('informacion_sistema.csv', 'w', newline='') as archivocsv:
        fieldnames = datos.keys()
        escribir = csv.DictWriter(archivocsv, fieldnames=fieldnames)
        
        escribir.writeheader()
        for i in range(maxDatos):
            # En caso de que una columna no tenga valores pondrá N/A.
            row = {key: datos[key][i] if i < len(datos[key]) else "N/A" for key in fieldnames}
            escribir.writerow(row)

def crearHTML (datos, maxDatos):
    # Creamos un archivo html y almacenamos los datos de cada columna. Se escribe todo el html en el archivo y luego se edita con la informacion necesaria.
    with open('informacion_sistema.html', 'w') as html:
        html.write('<!DOCTYPE html>\n')
        html.write('<html lang="en">\n')
        html.write('<head>\n')
        html.write('<meta charset="UTF-8">\n')
        html.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        html.write('<title>Informacion del Sistema</title>\n')
        html.write('<style>\n')
        html.write('body {\n')
        html.write('font-family: Arial, sans-serif;\n')
        html.write('background-color: #f4f4f4;\n')
        html.write('margin: 0;\n')
        html.write('padding: 0;\n')
        html.write('}\n')
        html.write('h1 {\n')
        html.write('text-align: center;\n')
        html.write('margin-top: 20px;\n')
        html.write('}\n')
        html.write('table {\n')
        html.write('border-collapse: collapse;\n')
        html.write('width: 80%;\n')
        html.write('margin: 20px auto;\n')
        html.write('background-color: #fff;\n')
        html.write('box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);\n')
        html.write('border: 2px solid #ddd;\n')
        html.write('}\n')
        html.write('th, td {\n')
        html.write('padding: 10px;\n')
        html.write('text-align: left;\n')
        html.write('border: 2px solid #808080;\n')
        html.write('}\n')
        html.write('th {\n')
        html.write('background-color: #f2f2f2;\n')
        html.write('color: #333;\n')
        html.write('}\n')
        html.write('tr:hover {\n')
        html.write('background-color: #f2f2f2;\n')
        html.write('}\n')
        html.write('</style>\n')
        html.write('</head>\n')
        html.write('<body>\n')
        html.write('<h1>Informacion del Sistema</h1>\n')
        html.write('<table border="1">\n')
        html.write('<tr>\n')
        # Creamos la cabecera de la tabla. Son th.
        for key in datos:
            html.write('<th>{}</th>\n'.format(key))
        html.write('</tr>\n')
        # Se agregan los datos hasta que llega al numero total de datos en la lista. Creando los td necesarios por cada uno de ellos.
        for i in range(maxDatos):
            html.write('<tr>\n')
            for key in datos:
                html.write('<td>{}</td>\n'.format(datos[key][i] if i < len(datos[key]) else "N/A"))
            html.write('</tr>\n')

        html.write('</table>\n')
        html.write('</body>\n')
        html.write('</html>\n')

# Parametros que le pedimos al usuario
ip = input('Introduce la IP que quieras analizar (ex.192.168.1.28): ')
username = input('Introduce el nombre de usuario: ')
password = input('Introduce la contraseña: ')
output = input('¿Que quieres crear (CSV/HTML/TODO)?: ')
port=22

datos, maxDatos = sacarInformacion(ip, port, username, password)

# Comprobador
if output == 'TODO':
    crearCSV(datos, maxDatos)
    crearHTML(datos, maxDatos)
elif output == 'CSV':
    crearCSV(datos, maxDatos)
elif output == 'HTML':
    crearHTML(datos, maxDatos)
else:
    print('No se ha seleccionado una opción válida')