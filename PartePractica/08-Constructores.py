#Método Constructor

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def descripcion(self):
        return "Nombre: {} Apellido: {} Su edad es: {}".format(self.nombre, self.apellido, self.edad)

    def comentario(self, frase):
        return "{} dice: {}".format(self.nombre, frase)

doctor = Persona("Elias", "Franco", 20)
print(doctor.descripcion())
print(doctor.comentario("Hola qué tal"))


#Modificar un atributo, sirve para corregir errores.
class Email: 
     def __init__(self):
          self.enviado = False
     def enviar_correo(self):
          self.enviado = True


mi_correo = Email()
print(mi_correo.enviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)




