#simulo las entradas de la funcion para hacer las pruebas
start = "2:35 PM"
duration = "23:15"
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
tarde = 'AM'
dias = 0 

#suma de minutos
suma_minutos = int(new_start[1]) + int(new_duration[1])

if suma_minutos > 60:
    suma_horas += 1
    suma_minutos = suma_minutos - 60
elif 0 < suma_minutos < 60:
    pass
else:
    print("algo raro pasa con los minutos")

#sumo las horas
#si las horas son 12, parto desde 0
if int(new_start[0]) == 12:
    new_start[0] = 0

if new_start[2]=='PM':
    suma_horas = suma_horas + 12

#la variable suma_horas viene acarreando lo acumulado en la suma de minutos (si es que pasaron más de una hora) y la suma de 12 horas si es PM
suma_horas = suma_horas + int(new_start[0]) + int(new_duration[0])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

"""#cantidad de dias
dias = dias + round(int(suma_horas)/24)
print(f'{dias} después')"""

#voy restando de a 24 horas y sumando días a la cuenta. Esto me va a dar la cantidad de días y un horario en formato 24hs
while suma_horas > 24:
    suma_horas = suma_horas - 24
    dias +=1

#separar PM/AM
if suma_horas > 12:
    suma_horas = suma_horas - 12
    tarde ='PM'
elif 0 < suma_horas < 12:
    tarde ='AM'
else:
    print('Algo mal pasa con AM/PM')

#impresiones de prueba
print(f'{str(suma_horas)}:{suma_minutos} {tarde}')
print(f'{dias} later')