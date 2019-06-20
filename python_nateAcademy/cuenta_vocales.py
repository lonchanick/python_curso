
frase = input("Escribe una frase")
vocales = ["a","e","i","o","u"]

n_vocales = 0
n_consonantes = 0

for letra in frase:
	if letra in vocales:
		n_vocales +=1
	else:
		n_consonantes+=1

print("numero de vocales: {}".format(n_vocales))
print("numero de consonantes: {}".format(n_consonantes))
