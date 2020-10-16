dolares = float(input("Por favor ingresar la cantidad de dólares\n"))
tasa = float(input("Por favor poner la tasa de cambio \n"))
pesos = dolares * tasa

print(" Teniendo en cuenta USD " + str(dolares)+ " a una tasa de  " + str(tasa)+ " Ud. tendría COP " + str(pesos))