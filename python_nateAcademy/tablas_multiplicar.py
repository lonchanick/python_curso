user_input = int(input("Ingresa el numero de la tabla"))

for x in range(1,11):
	print("{} * {} = {}".format(user_input,x,(x*user_input)))