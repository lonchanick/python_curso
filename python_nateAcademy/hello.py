
numberToGuess = 1;

for x in xrange(1,10):
	user_number = input("Cual es tu numero?: ");
	if numberToGuess == user_number:
		print("has ganado")
	else:
		print("has perdido")