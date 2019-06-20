n_espacios = 0
n_comas = 0
n_puntos = 0
indice_for = 0

frase = input("ingrese una frase: ")

for x in frase:
	if frase[indice_for] ==" ":
		n_espacios+=1
	if frase[indice_for] ==",":
		n_comas+=1
	if frase[indice_for] ==".":
		n_puntos+=1
		
	indice_for+=1

print("espacios: {} Comas: {} Puntos: {}".format(n_espacios, n_comas, n_puntos))