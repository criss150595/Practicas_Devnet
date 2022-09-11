class Persona():
    def __init__(self, nombre, edad): # Inicializador de atributos (Constructor)
        self.nombre = nombre
        self.edad = edad
        

class Empleado(Persona):
    def __init__(self, nombre , edad , sueldo):
        super().__init__(nombre , edad)
        self.sueldo = sueldo


Empleado1 = Empleado ("Juan",35,5000)
print(f"Datos del Empleado : El nombre es {Empleado1.nombre}   Su edad es {Empleado1.edad} El sueldo que percibe es  {Empleado1.sueldo}")



class Router:
    def __init__(self, Marca , Modelo , Version, Ipadd, Mask):
        self.Marca = Marca
        self.Modelo = Modelo
        self.Version = Version
        self.Ipadd = Ipadd
        self.Mask = Mask

class Switch(Router):
    def __init__(self, Marca, Modelo, Version, Ipadd, Mask, vlans):
        super().__init__(Marca, Modelo, Version, Ipadd, Mask)
        self.vlans = vlans

SW1 = Switch("Cisco","Catalyst","2.2.2","10.10.10.10","/24","10")
print(SW1.Marca,SW1.Modelo)

class Firewall(Router):
    def __init__(self, Marca, Modelo, Version, Ipadd, Mask, Tipo):
        super().__init__(Marca, Modelo, Version, Ipadd, Mask)
        self.tipo = Tipo

class Access_Point(Router):
    def __init__(self, Marca, Modelo, Version, Ipadd, Mask, Frecuencia):
        super().__init__(Marca, Modelo, Version, Ipadd, Mask)
        self.Frecuencia = Frecuencia
