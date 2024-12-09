class Empleado():
    def __init__(self, nombre, salario):
        self.__nombre = nombre 
        self.__salario = salario

#Encapsulamos los métodos
    def __getnombre(self):
        return self.__nombre

    def __getsalario(self):
        return self.__salario

    def __setnombre(self, nombre):
        self.__nombre = nombre

    def __setsalario(self, salario):
         self.__salario = salario

    def __delnombre(self):
        del self.__nombre

    def __delsalario(self):
        del self.__salario

    nombre = property(fget= __getnombre, 
                      fset= __setnombre,
                      fdel= __delnombre,
                      doc = "Soy la propiedad del 'nombre'" )

    salario = property(fget= __getsalario)

empleado_uno = Empleado("Marquihos", 30000)
empleado_uno.nombre = "Edgar"
print(empleado_uno.nombre, empleado_uno.salario)

help(empleado_uno)
      # Help es para ver la documentación del objeto empleado_uno.