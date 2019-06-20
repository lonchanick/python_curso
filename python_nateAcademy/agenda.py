
import os

agenda = dict()

nombre_contacto =""
numero_contacto =""
op =""

while op!="S":
	
	op = input("Que es lo que quieres hacer (Añadir numero [A] / Consultar numero [C] / Mostrar contactos [M] / Salir [S]) ")

	if op == "A":
		os.system('clear')
		print("Agregando un numero nuevo")
		print("---------------------------")
		nombre_contacto = input("Nombre: ")
		numero_contacto = input("Número: ")
		agenda[nombre_contacto] = numero_contacto
		print()

	if op == "C":
		os.system('clear')
		print("   Buscando un numero")
		print("---------------------------")

		nombre_a_buscar = input ("¿El numero de quien necesitas? ")
		print(agenda[nombre_a_buscar])
		input()
	
	if op == "M":
		os.system('clear')
		print("   CONTACTOS ")
		print("-----------------------")
		print(agenda)
		input()

	if op == "S":
		print("Saliendo ...")

	os.system('clear')
	

