import csv
import paramiko

ip = input('Introduce la IP que quieras analizar (ex.192.168.1.28): ')
username = input('Introduce el nombre de usuario: ')
password = input('Introduce la contraseña: ')
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

for key in data:
    if not data[key]:
        data[key] = ["N/A"]

# Find the maximum length among the lists
num_records = max(len(data[key]) for key in data)

with open('informacion_sistema.csv', 'w', newline='') as csvfile:
    fieldnames = data.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for i in range(num_records):
        row = {key: data[key][i] if i < len(data[key]) else "N/A" for key in fieldnames}
        writer.writerow(row)
    
ssh_client.close()