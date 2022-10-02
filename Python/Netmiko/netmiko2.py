# Importando las librerias
from ast import parse
from textwrap import indent
import Netmiko
from Netmiko import ConnectHandler
import json


# Declaramos el dispositivo que sera configurado

ios1 = {
    "device_type": "cisco_ios",
    "host": "192.168.138.131",
    "username": "cisco",
    "password": "cisco",
    "session_log": "ios1.txt"
}



net_connect = ConnectHandler(**ios1)
command = (
            "show environment summary",
            "show cdp neighbor",
            "show cdp neighbor detail",
            "show interface description",
            "show inventory",
            "show version",
            "dir all",
            "show bootvar",
            "show running-config",
            "Show run | include classe-map", 
            "Show run | include policy-map",
            "show logging",
            "show ntp config",
            "show ip mroute",
            "Show running | i  username",
            "Show ip interface brief", 
            "Show run  interface Loopback0", 
            "Show ip ospf neighbor", 
            "Show ip bgp summary", 
            "Show run | include mpls", 
            "Show mpls ldp neighbor | in Peer", 
            "Show ip route",
            "Show ip route 200.87.254.101",
            "Show ip bgp nei"
)

with ConnectHandler (**ios1) as net_connect:
    for command in command:
        output = net_connect.send_command(command)
