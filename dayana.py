class poligono:

    def __init__(self,b,h):
        self.b = b
        self.h = h

class Rectangulo(poligono):

    def area(self):
        return self.b * self.h

class Triangulo(poligono):

    def area(self):
        return (self.b * self.h) / 2

rectangulo = Rectangulo(20,10)
triangulo = Triangulo(20,12)

print("Area del rectangulo: ", rectangulo.area())
print("Area del triangulo:", triangulo.area())
