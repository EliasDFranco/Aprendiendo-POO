#f-Strings

curso = "60 Ing. Informática"
nombre = "Elias"
edad = 20
print(f"Alumnos de la carrera de {curso}")
print(F"El nombre del alumno: {nombre} y su edad: {edad}")


class Alumnos:
     def __init__(self, nombre, apellido, edad):
        self. nombre = nombre
        self.apellido = apellido 
        self.edad = edad 

     def __str__(self):
          return f"{self.nombre} {self.apellido} {self.edad}"


nuevo_estudiante = Alumnos('Elias', 'Franco', 20)
print(f"{nuevo_estudiante}")
