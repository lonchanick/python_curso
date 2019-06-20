user_input = input("Ingrese una frase: ")

indice = 0
contador_mayusculas = 0
x = 0

for x in user_input:
	if user_input[indice].isupper():
		contador_mayusculas+=1
	indice+=1

print(contador_mayusculas)