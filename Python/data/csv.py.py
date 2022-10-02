#!/usr/bin

import os
import csv
"""
print("Please add a new router to the list")
hostname = input("What is the hostname? " + "")
ip = input("What is the ip address? " + "")
location = input("What is the location? " + "")
router = [hostname, ip, location]

with open("Python\\data\\routerlist.csv", "a") as data:
    csv_writer = csv.writer(data)
    csv_writer.writerow(router)
"""

# Imprimir el archivo .csv como csv
print("*"*30)
print("Se leera el archivo .csv como CSV")
print("*"*30)
with open("Python\\data\\routerlist.csv") as samplefile:
    samplereader = csv.reader(samplefile)
    sampledata = list(samplereader)
    print(sampledata)

#  Imprimir el archivo .csv como lista
print("*"*30)
print("Se imprimira el file .csv como lista")
print("*"*30)
with open("Python\\data\\routerlist.csv") as samplefile:
    samplereader = csv.reader(samplefile)
    for row in samplereader:
        print(row)

# Imprimir el archivo .csv de manera iterativa
print("*"*30)
print("Se imprimira de manera iterativa")
print("*"*30)
with open("Python\\data\\routerlist.csv") as samplefile:
    samplereader = csv.reader(samplefile)
    for row in samplereader:
        router = row[0]
        location = row[2]
        ip = row[1]
        print(f"{router} is in {location.rstrip()} and has IP {ip.rstrip()}.")
# Imprimir el archivo .csv como diccionario
print("*"*30)
print("Se leera el archivo .csv como tupla")
print("*"*30)
with open("Python\\data\\routerlist.csv") as samplefile:
    samplereader = csv.reader(samplefile)
    sampledata = tuple(samplereader)
    print(sampledata)
