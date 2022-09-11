

class Router:
    def __init__(self, Marca , Modelo , Version, Ipadd, Mask):
        self.Marca = Marca
        self.Modelo = Modelo
        self.Version = Version
        self.Ipadd = Ipadd
        self.Mask = Mask
    def mostrar_detalle(self):
        print(f" Detalles del Router : {self.Marca} {self.Modelo} {self.Version} {self.Ipadd} {self.Mask}")
    def mostrar_marca(self):
        print(f"La marca del Router es : {self.Marca}")
    def getdef(self):
        descripcion =   f'Router Model :            {self.Modelo}\n'\
                        f'Software Version :        {self.Version}\n'\
                        f'Router Management Address:{self.Ipadd}'
        return descripcion


Router1 = Router("Cisco","NX-OS","7.2","192.168.1.1","255.255.255.0")
Router1.mostrar_detalle()
Router1.mostrar_marca()
Router1.Loopback = "1.1.1.1"
print(f"La Loopback es : {Router1.Loopback}")
Router2 = Router("Huawei" ,"HW-920" , "7.2.1" , "192.168.6.1" , "255.255.255.0")
Router2.mostrar_detalle()
Router2.mostrar_marca()
Router3 = Router("Nokia" , "SAR-700" , "6.2.0" , "192.168.20.1" , "255.255.255.0")
Router3.mostrar_detalle()
Router3.mostrar_marca()
Router4 = Router("Juniper","JN-0S 700","3.2.2","192.168.30.1","255.255.255.0")
Router4.mostrar_detalle()
Router4.mostrar_marca()
print(Router4.getdef())
pass


class Switch:
    def __init__(self,  Marca , Modelo , Version, Ipadd, Mask):
        self.Marca = Marca
        self.Modelo = Modelo
        self.Version = Version
        self.Ipadd = Ipadd
        self.Mask = Mask
    def mostrar_detalle(self):
        print(f"Detalles del Switch : {self.Marca} {self.Modelo} {self.Version} {self.Ipadd} {self.Mask}")
    def mostrar_marca(self):
        print(f"La marca del Switch: {self.Marca}")    
    

Switch1 = Switch("Aruba","Catalyst 960","2.6","192.168.100.1","255.255.255.0")
Switch1.mostrar_detalle()
Switch1.mostrar_marca()

    