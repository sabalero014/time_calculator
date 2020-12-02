def add_time(start, duration):
    #primero: separar la hora en partes.
    #reemplazo el espacio antes de AM/PM por un ":", así me es más fácil separar.
    #separo finalmente
    new_start = start.replace(" ",":").split(":")

    #separo también DURATION
    new_duration = duration.split(":")

    #suma de minutos
    duracion_horas = 0 #ya dejo planteada la duración en horas para poder sumarla en el condicional
    duracion_minutos = new_start[1] + new_duration[1]
    if duracion_minutos > 60:
        duracion_horas += 1
        duracion_minutos = duracion_minutos - 60
    elif 0 < duracion_minutos < 60:
        pass
    else:
        print("algo raro pasa con los minutos")
    
    #diferencio entre AM y PM
    if new_start =="PM":
        duracion_horas = duracion_horas + 12
    else:
        pass
    
    #sumo las horas
    duracion_horas = duracion_horas + new_start[0] + new_duration[0]
    

    return new_time