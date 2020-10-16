from datetime import date

anio_nacim = int(input("Ingrese año de nacimiento \n"))
mes_nacim = int(input("Ingrese mes de nacimiento \n"))
dia_nacim = int(input("Ingrese día de nacimiento \n"))


fecha_nacim = date(anio_nacim, mes_nacim, dia_nacim)

today = date.today()

diferencia_anios = (today.year-fecha_nacim.year)*12
diferencia_meses = (today.month-fecha_nacim.month)
diferecia_total = (diferencia_anios+diferencia_meses)

print("Desde la fecha de nacimiento del usuario han pasado " + str(diferecia_total)+ " meses")


