start = "12:35 AM"
duration = "3:15"
new_start = start.replace(" ",":").split(":")
#separo también DURATION
new_duration = duration.split(":")

#lista de valores sumados
#formato final: [hora, minutos, AM/PM, días]
sumados = []

#suma de minutos
suma_horas = 0 #ya dejo planteada la duración en horas para poder sumarla en el condicional
suma_minutos = int(new_start[1]) + int(new_duration[1])

if suma_minutos > 60:
    suma_horas += 1
    suma_minutos = suma_minutos - 60
elif 0 < suma_minutos < 60:
    pass
else:
    print("algo raro pasa con los minutos")

#diferencio entre AM y PM
if new_start [2] =="PM":
    suma_horas = suma_horas + 12
else:
    pass

#sumo las horas
suma_horas = suma_horas + int(new_start[0]) + int(new_duration[0])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

#lista de los valores sumados nuevamente. Va al final de todo, con las variables copiadas
sumados = [suma_horas,suma_minutos]
#faltan 2 valores todavia

#impresiones de prueba
print(suma_minutos)
print(suma_horas)