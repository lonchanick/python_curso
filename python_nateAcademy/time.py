from time import sleep
import datetime

NIGHT_START = 19
DAY_STARS = 8
HOUR_DURATION = 1

def main():
	current_time = datetime.datetime.now()
	while True:
		sleep(HOUR_DURATION)
		current_time += datetime.timedelta(hours=1)

		if current_time.hour >= NIGHT_START or current_time.hour <= DAY_STARS:
			day_night_lable = "Noche"
		else:
			day_night_lable = "Dia"

		time_text = "La hora actual es {}, es de {}\n".format(current_time,day_night_lable)
		with open("horas.txt","a") as hours_file:
			hours_file.write(time_text)
			print(time_text)

if __name__ == "__main__":
	main()
	pass