class Persona:

    def __init__(self,cedula,nombre,apellido):
        self.__cedula = cedula
        self.nombre = nombre
        self.apellido = apellido

    def setCedula(self,cedula):
        self.__cedula=cedula

    def getCedula(self):
        return self.__cedula

    def getData(self):
        return self.__cedula+" "+self.nombre+" "+self.apellido

class Estudiante(Persona):

    def __init__(self,cedula,nombre, apellido,cod_mat):
        Persona.__init__(self,cedula,nombre,apellido)
        self.__cod_mat=cod_mat

    def setCod_mat(self,codigo):
        self.__cod_mat=codigo

    def getCod_mat(self):
        return self.__cod_mat

    def getData(self):
        return self.getCedula()+" "+self.nombre+" "+\
               self.apellido+" "+str(self.__cod_mat)

class Docente(Persona):

    def __init__(self,cedula,nombre,apellido,gestoria):
        Persona.__init__(self,cedula,nombre,apellido)
        self.gestoria = gestoria

    def getData(self):
        return self.getCedula()+" "+self.nombre+" "+\
               self.apellido+" "+self.gestoria

class Institucion:

    def __init__(self,nombre,direccion, tipo):
        self.nombre = nombre
        self.direccion= direccion
        self.__tipo = tipo

    def setTipo(self,tipo):
        self.__tipo=tipo

    def getTipo(self):
        return self.__tipo

    def getData(self):
        return self.nombre+" "+self.direccion+" "+self.__tipo

class Materia:

    def __init__(self,cod_mate,nombre):
        self.__cod_mate= cod_mate
        self.nombre= nombre

    def setCod_mate(self,codigo):
        self.__cod_mate=codigo

    def getCod_mat(self):
        return self.__cod_mate

    def getData(self):
        return self.__cod_mate+" "+self.nombre

class Carrera:

    def __init__(self,cod_carr,nombre):
        self.__cod_carr = cod_carr
        self.nombre = nombre

    def setCod_carrera(self,codigo):
        self.__cod_carr= codigo

    def getCod_carrera(self):
        return self.__cod_carr

    def getData(self):
        return self.__cod_carr+" "+self.nombre




