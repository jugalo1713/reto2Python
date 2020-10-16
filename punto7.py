from math import tan
from math import radians
from math import pi

altura = float(20)
angulo = float(22)
radianes = radians(angulo)
tangente = tan(radianes)

longitud = round((altura/tangente),2)

print("La longitud de la sombra de un edificio de 20 Metros es de: "+ str(longitud) + " Metros si el ángulo del sol es de 22° ")

