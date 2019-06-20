import os

user_input = ""

while (user_input != "EXIT"):
	user_input = input ("-> ")
	resultado = user_input.replace("a","i")
	resultado = resultado.replace("e","i")
	resultado = resultado.replace("o","i")
	resultado = resultado.replace("u","i")
	print(" -> {}".format(resultado))
	input()
	os.system('clear')