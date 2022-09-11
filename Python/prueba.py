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