from math import pi

diametro = float(0.50)

largo_vuelta = pi * diametro

vueltas = round((1000/largo_vuelta),2)


print("El número de vueltas que da una rueda en 1 km si su diametro  es de 50 cm sería "+ str(vueltas)+ " vueltas")
