#Métodos Clase y Estático
#Clase;
class Pastel:
    def __init__(self, ingredientes):
         self.ingredientes = ingredientes

    def __repr__(self):
         return f"Pastel({self.ingredientes})"

    @classmethod 
    def Pastel_frutilla(cls):
         return cls(["Harina","Leche","Frutilla"])

    @classmethod
    def Pastel_chocolate(cls):
         return cls(["Harina", "Leche", "Chocolate"])

print(Pastel.Pastel_chocolate())
print(Pastel.Pastel_frutilla())

#Estático;
import math
class Alfajor: 
     def __init__(self, ingredientes, tamaño):
          self.ingredientes = ingredientes
          self.tamaño = tamaño
     
     def __repr__(self):
         return (f"Alfajor({self.ingredientes}, "f"{self.tamaño})")
     
     def area(self):
         return self.tamaño_area(self.tamaño)

     @staticmethod
     def tamaño_area(Area):
          return Area ** 2 * math.pi

nuevo_alfajor = Alfajor(["Maicena", "Azúcar", "Yemas de huevo", "Harina", "Dulce de leche", "Polvo de Hornear"], 6)
print(nuevo_alfajor.ingredientes)
print(nuevo_alfajor.tamaño)
print(nuevo_alfajor.tamaño_area(12))