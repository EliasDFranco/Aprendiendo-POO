#Herencia ejercicio practico
import math
class Calculadora: #Clase Padre 
    def __init__(self, numero):
        self.num = numero
        self.datos = [0 for i in range(numero)]

    def ingresar_dato(self):
        self.dato = [int(input("Ingrese el número"+str(i+1)+ "= "))for i in range(self.num)]

class operaciones(Calculadora):  #Clase Hija
    def __init__(self):
        Calculadora.__init__(self,2)  #Aqui limitamos a solo 2 valores para nuestra calculadora
    def suma(self):
        valorA, valorB = self.datos
        sum = valorA + valorB
        print("El resultado de la suma es: ", sum)
  
    def resta(self):
        valorA, valorB = self.datos
        res = valorA - valorB
        print("El resultado de la resta es: ", res)
 
    def division(self):
        valorA, valorB = self.datos
        div = valorA / valorB 
        print("El resultado de la división es: ", div)
        
    def multiplicacion(self):
        valorA, valorB = self.datos
        multi = valorA * valorB 
        print("El resultado de la multiplicación es: ", multi)

class raizcuadrada(Calculadora): #Este es otro hijo de la clase Calculadora
    def __init__(self):
        Calculadora.__init__(self,1) # Aqui solo necesitamos 1 valor para su dicha raiz
    
    def cuadrada(self):
        import math #Importamos esta libreria que ayuda a usar funciones matemáticas
        valorA = self.datos
        print("El resultado de la raiz cuadrada es: ",math.sqrt(valorA))

objeto = operaciones()  #Aqui creamos el objeto ejemplo

print(isinstance(objeto,operaciones))  #isinstance es una función integrada que sirve para verificar si un objeto pertenece a una clase o a una tupla de clases específicas.



print(issubclass(operaciones,Calculadora)) #issubclass es una función integrada que sirve paraverificar si una clase es una subclase de otra clase o de una tupla de clases específicas.


 

