# Importando las librerias
from ast import parse
from distutils.cmd import Command
from textwrap import indent
import netmiko
from netmiko import ConnectHandler
import json


# Declaramos el dispositivo que sera configurado

ios1 = {
    "device_type": "cisco_ios",
    "host": "192.168.138.131",
    "username": "cisco",
    "password": "cisco",
    "session_log": "netmiko3.txt"
}


net_connect = ConnectHandler(**ios1)

command = "show platform"
output = net_connect.send_command(command)
print(output)