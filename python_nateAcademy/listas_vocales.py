
vocales = ["a","e","i","o","u"]

user_input = input("Ingresa una frase: ")
total_vocales = []
indice = 0

for x in user_input:
	if user_input[indice] in vocales:
		total_vocales.append(user_input[indice])
	indice+=1

print("Esta son las vocales encontradas en la frase ingresada: \n   : {}".format(total_vocales))