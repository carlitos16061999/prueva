class Empresa(object):
    def __init__(self,cargo,sueldo):
        self.cargo = cargo
        self.sueldo = sueldo

    def Cargo (self):
        print('Su cargo es de: ',self.cargo,' y su seldo es de: ',self.sueldo)


class Programador(Empresa):
    def __init__ (self,cargo,sueldo,empleado1):
        self.empleado1 = '2'
        Empresa.__init__(self,cargo,sueldo)
        self.cargo = str('Programdor')
        self.sueldo = str('160')

    def programador (self):
        return Empresa.Cargo(self)
    
class Ingeniero(Empresa):
    def __init__ (self,cargo,sueldo,empleado1):
        self.empleado1 = '1'
        Empresa.__init__(self,cargo,sueldo)
        self.cargo = str('Ingeniero')
        self.sueldo = str('200')


    def ingeniero (self):
        return Empresa.Cargo(self)
    