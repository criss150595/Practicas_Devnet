from ast import parse
from textwrap import indent
import netmiko
from netmiko import ConnectHandler
from getpass import getpass
import json


secret = getpass("Enter secret: ")

# Declaramos el dispositivo que sera configurado

ios1 = {
    "device_type": "cisco_ios",
    "host": "181.115.255.238",
    "username": "vacac",
    "password": "Paramore1505",
    "session_log": "Mafume.txt",
    "secret": "secret"
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
    "show running-config interface loopback 0",
    "Show ip ospf neighbor",
    "Show ip bgp summary",
    "Show run | include mpls",
    "Show mpls ldp neighbor | in Peer",
    "Show ip route",
    "Show ip route 200.87.254.101",
    "Show ip bgp nei"
)

# Call 'enable()' method to elevate privileges
#net_connect.enable()
#print(net_connect.find_prompt())

with ConnectHandler(**ios1) as net_connect:
    for command in command:
        output = net_connect.send_command(command)
