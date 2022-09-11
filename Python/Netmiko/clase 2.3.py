import paramiko, getpass, time

from multiprocessing import connection
from sys import setrecursionlimit, stderr, stdin, stdout
import paramiko,time,pprint


# Conexion SSH
connection = paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Introduciondo la IP-USUARIO-PASSWORD
connection.connect('192.168.138.131', username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
new_connection = connection.invoke_shell()
output = new_connection.recv(50000)
print(output)
################################################


devices = {'iosv-1': {'ip': '192.168.138.131'}}
commands = ['show interface\n', 'show run\n']

username = input('Username: ')
password = getpass.getpass('Password: ')

max_buffer = 65535

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)

# Starts the loop for devices
for device in devices.keys(): 
    outputFileName = device + '_output.txt'
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'], username=username, password=password, look_for_keys=False, allow_agent=False)
    new_connection = connection.invoke_shell()
    output = clear_buffer(new_connection)
    time.sleep(2)
    new_connection.send("terminal length 0\n")
    output = clear_buffer(new_connection)

    with open(outputFileName, 'wb') as f:
        for command in commands:
            new_connection.send(command)
            time.sleep(2)
            output = new_connection.recv(max_buffer)
            print(output)
            f.write(output)
    
    new_connection.close()