import datetime

year = datetime.datetime.today().year
month = datetime.datetime.today().month
day = datetime.datetime.today().day

horaSalida = datetime.datetime(year= year, month= month, day= day, hour=19, minute=00)
horaActual = datetime.datetime.now()

diferencia = horaSalida - horaActual

if horaActual.time() > horaSalida.time():
    print("Ya es hora de salir")
else:
    print("Todavia falta ", diferencia)

