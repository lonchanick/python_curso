
lista_numeros = [1,23,512,444,77,23,45,67,23,572]

mas_grande = lista_numeros[0];
indice = 0

for x in range(1,11):
	if(lista_numeros[indice]>mas_grande):
		mas_grande = lista_numeros[indice]
	indice += 1

print(" El numero mayor es: {}".format(mas_grande))