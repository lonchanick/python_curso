import datetime
"""
year = int(input("Dime el año "))
month = int(input("Dime el mes "))
day = int(input("Dime el día  "))

user_date = datetime.datetime(year=year, month=month, day=day)
"""
fecha_actual = datetime.datetime.now()
manana = fecha_actual+datetime.timedelta(days=1)
print("Manñana sera {}".format(manana.strftime("%d de %m del %Y")))

inicio_de_manana = datetime.datetime(year=manana.year,month=manana.month,day=manana.day)

print("Mañana inicia: ".format(inicio_de_manana))

faltante = inicio_de_manana - fecha_actual 

print("faltan {} días y {} horas para mañana".format(faltante.days,(faltante.total_seconds()/3600)))

