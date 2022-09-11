# Importando las librerias
from ast import parse
from textwrap import indent
import netmiko
from netmiko import ConnectHandler
import json


# Declaramos el dispositivo que sera configurado

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.138.131",
    username="cisco",
    password="cisco",
    session_log =  "output.txt"
)


# La variable output contendra el comando que sera enviado al dispositivo
# la funcion net_connect.send_command, contiene el comando
output = net_connect.send_command("show interfaces")
print(output)

# Con config_commands, se introducen comandos en el modo de configuracion de cisco
config_commands = [ 'hostname Router2',
                    'router ospf 1',
                    'network 1.1.1.1 0.0.0.0 area 0',
                    'router-id 1.1.1.1']
# Se imprime el resultado
output = net_connect.send_config_set(config_commands)
print(output)

with net_connect as net_connect:
    output = net_connect.send_command(output)