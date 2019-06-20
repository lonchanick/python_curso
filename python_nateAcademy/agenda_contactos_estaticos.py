


"""
este fue mi intento por seguile los pasos a nate durante el video 
este codigo se fue a la mierdita .. 


"""



import os
from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

MENU_OPTIONS = [ ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]

def show_menu():
	
	#os.system("clear")
	print("Opciones disponibles: ")
	print("1 - Añadir contactos ")
	print("2 - Eliminar contactos ")
	print("3 - Buscar contactos ")
	print("4 - Exportar contactos CSV ")
	print("5 - Salir contactos ")

	selected_action = ""
	while not selected_action.isdigit() or (selected_action.isdigit and int(selected_action) not in MENU_OPTIONS):
		selected_action = input("¿Que opcion deseas? ")

	return int(selected_action)


def add_contact(contacts):
	#os.system("clear")
	print("Añadir contacto")
	contact = {
		"name": input("Nombre: "),
		"phone": input("Telefono: "),
		"email": input("Mail: ")
	}
	contacts.append(contact)
	print("Contacto agregado {}...".format(contact["name"]))
	sleep(2)

def remove_contact(contacts):
	print("Eliminar contactos")

def find_contact(contacts):
	print("Buscar contacto")
	search_term = input("Nombre del contacto: ")
	found_contacts =[]

	print("contactos encontrados")

	for contact in contacts:
		if contact["name"].find(search_term) >= 0:
			found_contacts.append(contact)
			print(contact["name"])

	return found_contacts

def export_contact():
	print("Exportar contacto")


def main():
	contacts = []
	action = show_menu()
	print("\nAccion seleccionada",action)

	while action != ACTION_EXIT:
		if action == ACTION_ADD_CONTACT:
			add_contact(contacts)
		elif action == ACTION_REMOVE_CONTACT:
			remove_contact(contacts)
		elif action == ACTION_FIND_CONTACT:
			find_contact(contacts)
		elif action == ACTION_EXPORT_CONTACT:
			export_contact()

		action != show_menu()


if __name__ =="__main__":
	main()