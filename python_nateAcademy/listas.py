lista = ["hola", "mundo", 2019, "Esmeraldas 16/04/2019", 1989]

cont = 0
numero_elemento =1;
input_usuario =""



input_usuario =input("Que necesitas comprar (Escribe FIN para salir)")

while input_usuario != "FIN":
	lista.append(input_usuario)
	input_usuario =input("Que necesitas comprar? (Escribe FIN para salir)")

tamano = len(lista)
print("Tu lista de compra es la siguiente: ")
while cont < tamano:
	print("Item num {} de la lista : {}".format(numero_elemento, lista[cont]))
	cont+=1
	numero_elemento+=1