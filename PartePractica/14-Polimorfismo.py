#Polimorfismo
class Animales:
    def __init__(self, nombre):
        self.nombre = nombre 
    def tipo_animnal(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
         print("Es un animal salvaje")

class Gato(Animales):
    def tipo_animal(self):
         print("Es un animal doméstico")
 

nuevo_animal = Leon("Simbad")
nuevo_animal.tipo_animal()

nuevo_animal2 = Gato("Puar")
nuevo_animal2.tipo_animal()


