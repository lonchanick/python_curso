
import datetime
import random

AVERAGE_LIFESPAM = 80
SMOKER_PENALIZATION = 10
DRINKER_PENALIZATION = 10
SEDENTARY_PENALIZATION = 20

def print_under_scores(param):
	print(param)
	print("-"*len(param))

def ask_yes_or_not(message):
	response = None
	while response != "S" and response != "N":
		response = input(message +"(S/N)")

	return response == "S"

print_under_scores ("Cuanto te queda de vide ¿?")
print("Contesta estas preguntas para hacer el calculo: ")
# birth_date = input("cual es tu fecha de nacimiento? (dd/mm/aa) ?")
birth_date = "10/8/1991"
birth_date = datetime.datetime.strptime(birth_date,"%d/%m/%Y")
years_lost = 0

"""
if ask_yes_or_not("Fumas? "):
	years_lost += SMOKER_PENALIZATION

if ask_yes_or_not("Bebes? "):
	years_lost += DRINKER_PENALIZATION

if not ask_yes_or_not("Haces deporte? "):
	years_lost += SEDENTARY_PENALIZATION
"""
years_lost = 40


lifespan = AVERAGE_LIFESPAM - years_lost
dead_day = birth_date + datetime.timedelta(days = lifespan * 365)
#dead_day = dead_day.strftime("%d/%m/%Y")
print("La fecha de tu muerte sera {}".format(dead_day.strftime("%d/%m/%Y")))

days_to_dead = dead_day - datetime.datetime.now()
print("Te quedan {} dias de vida modofaker".format(days_to_dead.days))
