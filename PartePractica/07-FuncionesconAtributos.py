#Funciones con Atributos
from traceback import print_tb


class  Persona:
    def __init__(self):
        self.edad = 27
        self.nombre = "Elias"
        self.pais = "Paraguay"

doctor = Persona()
print("La edad es ",doctor.edad )
print("La edad es: ", getattr(doctor,"edad")) #Aqui usamos getattr
print("Elnombre es: ",doctor.nombre)

print("El doctor tiene una edad??", hasattr(doctor, "edad")) #Aqui usamos hasattr
print('Nombre anterior: ', doctor.nombre)
setattr(doctor, 'nombre','Ariel') #Aqui usamos setattr
print('Nombre actualizado: ', doctor.nombre)

delattr(Persona, 'pais')
print(doctor.pais)
print(doctor.edad)

