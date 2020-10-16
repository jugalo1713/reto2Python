import statistics

espaniol = float(input("Por favor informar su nota de Español entre 1 y 5\n"))
matematica = float(input("Por favor informar su nota de matemática entre 1 y 5\n"))
economia = float(input("Por favor informar su nota de economía entre 1 y 5\n"))
programacion = float(input("Por favor informar su nota de programación entre 1 y 5\n"))
ingles = float(input("Por favor informar su nota de ingles entre 1 y 5\n"))

notas = [espaniol, matematica, economia, programacion, ingles]

promedio = statistics.mean(notas)

print("El promedio de notas es de " + str(promedio))