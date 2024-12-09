#Encapsulación
class Cliente:
    def __init__(self):
        self.__codigo = 192833913

    def __cuenta(self):
        print("Número de cuenta de banco")

    def getcodigo(self):
        return self.__codigo

persona = Cliente()      
#Objeto._nombreclase__nombreatributo
print(persona._Cliente__codigo)
persona._Cliente__cuenta()