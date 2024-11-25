#Métodos
# Métodos
class Matematicas: 
    def suma(self): 
        self.num_1 = 2
        self.num_2 = 2

operacion = Matematicas()
operacion.suma()
print(operacion.num_1 + operacion.num_2)

#Aqui vamos a llamar de nuevo a un método, pero con __init__(self)
class Ropa:
     def __init__(self):
         self.color = "Amarillo"
         self.marca = "Puma"
         self.talla = "MX"
         self.procedencia = "Italiana"

camisa = Ropa()
print(camisa.color)
print(camisa.marca)
print(camisa.talla)
print(camisa.procedencia)

class Calculadora:
    def __init__(self, num1, num2):
        self.suma = num1 + num2
        self.resta = num1 - num2
        self.multiplicación = num1 * num2
        self.división = num1 // num2

operacion = Calculadora(10,20)
print("Los resultados que vemos son;")
print(operacion.suma)
print(operacion.resta)
print(operacion.multiplicación)
print(operacion.división)






