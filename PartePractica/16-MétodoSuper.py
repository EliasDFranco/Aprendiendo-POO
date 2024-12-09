#Método Super()
class Mamifero():
    def __init__(self, nombre):
        print(nombre, "es un animal de sangre caliente")

class Leon(Mamifero):
    def __init__(self):
        print("El leon es un animal de 4 patas")
        super().__init__("Simba")
        #Tambien se puede usar Mamimero.__init__(self, "Simba"), pero el super() hace enfásis 
        #a la clase Mamimero.
        
nuevo_leon = Leon()