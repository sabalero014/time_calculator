#simulo las entradas de la funcion para hacer las pruebas
start = "2:35 PM"
duration = "3:15"
day = "MONDAY"
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
dias = 0 # es la suma de los dias de duración
el_dia = "" #a usar para poner el dia de la semana en que finaliza la tarea
num_dia = 0 # para elegir el numero de dia de la semana

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

#impresiones correctas
#despues reemplazar print por return
horario_fin = str(suma_horas)+":"+str(suma_minutos)+" "+tarde
days_later = "hola"
if dias == 1:
    days_later = " (next day)"
elif dias > 1:
    days_later = " ("+str(dias)+" days later)"
elif dias == 0:
    days_later = ""
else:
    days_later = "algo raro anda mal con los dias calculados"

#dias de la semana
#print(day)
if day == 1:
    #si no ingresa ningun nombre de dia, el valor toma 1 y en la oracion final queda sin naa
    el_dia = ""
elif day != 1:
    #primero: limpiar nombre del dia ingresado
    #print(type(day))
    dia_texto = str(day)
    dia_texto = dia_texto.lower()
    dia_texto = dia_texto.capitalize()
    
    #segundo: sacar numero de dia desde el diccionario
    num_dia = dias_sem[dia_texto]
    #print(f'numero de dia: {num_dia}')
    
    #tercero: sumar los dias para obtener luego del diccionario el nombre del dia
    dia_fin = num_dia + dias

    #cuarto: si es mayor que 7, hay que ir restando.
    while dia_fin > 7:
        dia_fin = dia_fin - 7
    #test print
    #print(f'dia de la semana en que finaliza: {dia_fin} - tipo: {type(dia_fin)}')

    #quinto: extraer del diccionario el nombre del dia a partir del valor.
    # https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
    #   5.a convertir los keys y values del diccionario en listas. Así puedo extraer index
    key_list = list(dias_sem.keys())
    val_list = list(dias_sem.values())
    #   5.b extraer el index del valor buscado
    position = val_list.index(dia_fin)
    #   5.c dia de la semana desde KEY
    el_dia = key_list[position]
    #print(f'dia extraido del condicional: {el_dia}')
    el_dia = ", "+key_list[position]

else:
    print("no agarró lo del dia de la semana")

print(horario_fin+el_dia+days_later)
new_time = horario_fin+el_dia+days_later