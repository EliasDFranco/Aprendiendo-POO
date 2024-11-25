#Herencia Múltiple
class Telefono: 
    def __init__(self):
        pass
    def llamar(self):
        print("Llamando....")

    def ocupado(self):
        print("Ocupado....")

class Camara:
    def __init__(self):
        pass 
    def fotografiar(self):
        print("Capturando fotos....")

class Reproduccion:
    def __Init__(self):
        pass
    def reproducirmp4(self):
        print("Reproduciendo videos....")
    def reproducirmp3(self):
        print("Reproduciendo música....")

class Smartphone(Telefono,Camara,Reproduccion):
     def __del__(self):
         print("Telefono apagado")

movil = Smartphone()
print(movil.llamar())
print(movil.fotografiar())
print(movil.reproducirmp3())
print(movil.reproducirmp4())