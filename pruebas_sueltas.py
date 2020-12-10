#simulo las entradas de la funcion para hacer las pruebas
start = "12:35 AM"
duration = "3:15"
day = 1
#hay que agregar dia a la DEF

#____________________________________
#acá arranca

#Separar las entradas de la funcion
new_start = start.replace(" ",":").split(":")
new_duration = duration.split(":")

#dias de la semana
dias_sem = {'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}

#variables
suma_horas = 0
suma_minutos = 0

#suma de minutos
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