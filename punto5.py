distancia_num = float(227940000)
distancia = "{:,}".format(distancia_num)
luz_num = float(299792.458)
luz = "{:,}".format(luz_num)
demora_num = round((distancia_num / luz_num),2)
demora = "{:,}".format(demora_num)
minutos = round((demora_num/60),2)


print("Marte se encuentra a una distancia del sol de " + distancia + " Km por lo que si la luz Viaja a " + luz + " Kilometros Por Segundo  Entonces esta se tarda en llegar a Marte " + demora + " Segundos lo cual equivale a " + str(minutos) + " minutos")

