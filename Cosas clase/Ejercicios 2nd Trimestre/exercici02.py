import csv
import paramiko

ip='10.100.64.56'
port=22
username='jvaliente-u2204'
password='hola1234'

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh_client.connect(ip, port, username, password)

    stdin, stdout, stderr = ssh_client.exec_command('ls')

    for line in stdout:
        print(line.strip())

    ssh_client.close()

except paramiko.AuthenticationException:
    print("Authentication failed, please check your credentials.")
except paramiko.SSHException as ssh_err:
    print(f"SSH connection failed: {ssh_err}")
except Exception as e:
    print(f"An error occurred: {e}")