
import datetime

def whatDayIs(param):
	if (param == 0):
		return("Lunes")
	elif (param == 1):
		return("Martes")
	elif (param == 2):
		return("Miercoles")
	elif (param == 3):
		return("Jueves")
	elif (param == 4):
		return("Viernes")
	elif (param == 5):
		return("Sabado")
	elif (param == 6):
		return("Domingo")

def hace_cuantos_dias():
	num_days = int(input("Cuantos días hacia atras deseas calcular gilipollas? "))
	fecha_actual = datetime.datetime.now()
	calculo = fecha_actual-datetime.timedelta(days=num_days)
	day = whatDayIs(calculo.weekday())
	print("Hace {} dias fue {} {}".format(num_days, day,calculo.strftime("%d,%m,%Y")))
#hace_cuantos_dias()

"""
#codigo para saber cuantos dias faltan para tu cumpleaños

user_birthday = datetime.datetime(year=2019, month=8, day=10)
fecha_actual = datetime.datetime.now()
faltante = user_birthday - fecha_actual

print("Faltan {} días para tu cumpleaños ".format(faltante.days))
""


