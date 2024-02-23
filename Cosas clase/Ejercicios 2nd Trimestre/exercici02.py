import csv
import paramiko

ip = input('Introduce la IP que quieras analizar (ex.192.168.1.28): ')
username = input('Introduce el nombre de usuario: ')
password = input('Introduce la contraseña: ')
output = input('¿Que quieres crear (CSV/HTML/TODO) ?: ')
port=22

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(ip, port, username, password)
stdin, ipv4_maquina, stderr = ssh_client.exec_command(r"ip addr | grep -Eo 'inet ([0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}' | grep -v 127.0.0.1 | awk '{print $2}'")
stdin, hostname_maquina, stderr = ssh_client.exec_command(r"hostname")
stdin, MAC_maquina, stderr = ssh_client.exec_command(r"ip addr | grep -Eo 'link/ether [^ ]+' | awk '{print $2}'")
stdin, procesador_maquina, stderr = ssh_client.exec_command(r"lshw | grep -A 4 '*-cpu' | grep 'producto:' | awk '{print $2, $3, $4, $5, $6, $7}'")
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

comprobarRoot_maquina = [True if int(line.strip()) == 1 else False for line in comprobarRoot_maquina]
puertoSSH_maquina = [True if int(line.strip()) == 2 else False for line in puertoSSH_maquina]
puertoHTTP_maquina = [True if int(line.strip()) == 1 else False for line in puertoHTTP_maquina]
puertoSMTP_IMAP_maquina = [True if int(line.strip()) == 1 else False for line in puertoSMTP_IMAP_maquina]

data = {
    "IP": [line.strip() for line in ipv4_maquina],
    "Hostname": [line.strip() for line in hostname_maquina],
    "MAC": [line.strip() for line in MAC_maquina],
    "Nombre Usuario": [username],
    "Nombre Procesador": [line.strip() for line in procesador_maquina],
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

num_records = max(len(data[key]) for key in data)

with open('informacion_sistema.csv', 'w', newline='') as csvfile:
    fieldnames = data.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for i in range(num_records):
        row = {key: data[key][i] if i < len(data[key]) else "N/A" for key in fieldnames}
        writer.writerow(row)

with open('informacion_sistema.html', 'w') as html_file:
    html_file.write('<!DOCTYPE html>\n')
    html_file.write('<html lang="en">\n')
    html_file.write('<head>\n')
    html_file.write('<meta charset="UTF-8">\n')
    html_file.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    html_file.write('<title>Información del Sistema</title>\n')
    html_file.write('<style>\n')
    html_file.write('body {\n')
    html_file.write('font-family: Arial, sans-serif;\n')
    html_file.write('background-color: #f4f4f4;\n')
    html_file.write('margin: 0;\n')
    html_file.write('padding: 0;\n')
    html_file.write('}\n')
    html_file.write('h1 {\n')
    html_file.write('text-align: center;\n')
    html_file.write('margin-top: 20px;\n')
    html_file.write('}\n')
    html_file.write('table {\n')
    html_file.write('border-collapse: collapse;\n')
    html_file.write('width: 80%;\n')
    html_file.write('margin: 20px auto;\n')
    html_file.write('background-color: #fff;\n')
    html_file.write('box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);\n')
    html_file.write('border: 2px solid #ddd;\n')
    html_file.write('}\n')
    html_file.write('th, td {\n')
    html_file.write('padding: 10px;\n')
    html_file.write('text-align: left;\n')
    html_file.write('border: 2px solid #808080;\n')
    html_file.write('}\n')
    html_file.write('th {\n')
    html_file.write('background-color: #f2f2f2;\n')
    html_file.write('color: #333;\n')
    html_file.write('}\n')
    html_file.write('tr:hover {\n')
    html_file.write('background-color: #f2f2f2;\n')
    html_file.write('}\n')
    html_file.write('</style>\n')
    html_file.write('</head>\n')
    html_file.write('<body>\n')
    html_file.write('<h1>Informacion del Sistema</h1>\n')
    html_file.write('<table border="1">\n')
    html_file.write('<tr>\n')
    for key in data:
        html_file.write('<th>{}</th>\n'.format(key))
    html_file.write('</tr>\n')

    # Escriu les dades a la taula
    for i in range(num_records):
        html_file.write('<tr>\n')
        for key in data:
            html_file.write('<td>{}</td>\n'.format(data[key][i] if i < len(data[key]) else "N/A"))
        html_file.write('</tr>\n')

    html_file.write('</table>\n')
    html_file.write('</body>\n')
    html_file.write('</html>\n')

    
ssh_client.close()