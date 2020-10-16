centigrados = float(input("Por favor ingresar los Grados Centigrados: \n"))
fahrenheit = centigrados * 1.8 + 32
rounded = round(fahrenheit,2)

print(str(centigrados)+ " Grados Centigrados Corresponden a "+ str(rounded)+ " Grados Fahrenheit")