class Tomate:
    def tipo(self):
        print("Vegetal")
    def color(self):
        print("Rojo")

class Naranja:
    def tipo(self):
        print("Fruta")
    def color(self):
        print("Anaranjado")

# Defino una función que recibe un objeto como argumento;
def funcion(objeto):
    objeto.tipo()
    objeto.color()

#Creo las instancias de las clases Tomate y Naranja;
nuevo_tomate = Tomate()
funcion(nuevo_tomate)

nueva_naranja = Naranja()
funcion(nueva_naranja) 
