
import os

agenda = dict()

nombre_amigo =""
anoNac_amigo =""
op =""

while op!="S":
	
	op = input("Que es lo que quieres hacer (Añadir Amigo [A] / Mostrar Amigos [M] / Salir [S]) ")

	if op == "A":
		os.system('clear')
		print("Agregando un Amigo")
		print("---------------------------")
		nombre_amigo = input("Nombre: ")
		anoNac_amigo = input("Año nac: ")
		agenda[nombre_amigo] = anoNac_amigo
		print() 
	
	if op == "M":
		os.system('clear')
		print("   AMIGOS ")
		print("-----------------------")
		for x in agenda:
			print("Nombre: ",x,"\nAño Nac: ",agenda[x])
		input()

	if op == "S":
		print("Saliendo ...")

	os.system('clear')