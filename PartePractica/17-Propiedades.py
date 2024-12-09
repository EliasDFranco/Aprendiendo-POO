#Propiedades 

class Empleado():
    def __init__(self, nombre, salario):
        self.__nombre = nombre 
        self.__salario = salario

#Hacemos un get | Get = Obtener
    def getnombre(self):
        return self.__nombre

    def getsalario(self):
        return self.__salario

#Hacemos un set | Define cómo modificar el atributo, añadiendo validaciones o lógica adicional.
    def setnombre(self, nombre):
        self.__nombre = nombre

    def setsalario(self, salario):
         self.__salario = salario

#Hacemos un del |  Define cómo eliminar el atributo, si es necesario.
    def delnombre(self):
        del self.__nombre

    def delsalario(self):
        del self.__salario

empleado_uno = Empleado("Elias", 3500000)
print(empleado_uno.getnombre(),',', empleado_uno.getsalario())

empleado_uno.setnombre("Juanes")
empleado_uno.setsalario(2000000)
print(empleado_uno.getnombre(),',', empleado_uno.getsalario())



        

