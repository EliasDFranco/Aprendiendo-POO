class Aves:
    def volar(self):
        print("La mayoría de aves pueden volar, pero algunas no")

class Aguila(Aves):
    def volar(self):
        print("Las aguilas si pueden volar")

class Avestruz(Aves):
    def volar(self):
        print("Las avestruces no pueden volar")

objeto_ave = Aves()
objeto_aguila = Aguila()
objeto_avestruz = Avestruz()

objeto_ave.volar()
objeto_aguila.volar()
objeto_avestruz.volar()