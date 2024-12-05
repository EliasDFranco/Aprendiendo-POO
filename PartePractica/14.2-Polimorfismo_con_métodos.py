class Paraguay:
    def capital(self):
        print("Asunción")
    def idioma(self):
        print("Castellano y Guaraní")
    def clima(self):
        print("Subtropical")

class Brasil:
    def capital(self):
        print("Brasilia")
    def idioma(self):
        print("Portugués")
    def clima(self):
        print("Cálido tropical")

#Las instancias de las clases de Paraguay y Brasil;
paraguayo = Paraguay()
brasilero = Brasil()

#Itero con un ciclo for sobre las instancias creadas anteriormente;
for pais in (paraguayo, brasilero):
     pais.capital()
     pais.idioma()
     pais.clima()




    