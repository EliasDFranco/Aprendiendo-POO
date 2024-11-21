#Herencia
class Pokemon: #Esta es la Clase Padre
    pass
    def __init__(self,nombre,tipo):
          self.nombre = nombre
          self.tipo = tipo 
    
    def descripcion(self):
          return "{} es un pokemon de tipo {}".format(self.nombre,self.tipo)

class Pikachu(Pokemon): #Esta es la Clase Hijo
    def ataque(self,tipo_ataque): #Aqui creamos un método dentro de una nueva clase
        return "{} tipo de ataque {}".format(self.nombre, tipo_ataque )

class Chadizar(Pokemon):
    def ataque(self,tipo_ataque):
        return "{} tipo de ataque ".format(self.nombre, tipo_ataque)

nuevo_pokemon = Pikachu("Kaku","Electrico")
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque("IMPACTO DE ELECTRICIDAD"))