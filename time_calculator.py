def add_time(start, duration):
    #primero: separar la hora en partes.
    #reemplazo el espacio antes de AM/PM por un ":", así me es más fácil separar.
    #separo finalmente
    new_start = start.replace(" ",":").split(":")

    #separo también DURATION
    new_duration = duration.split(":")

    return new_time