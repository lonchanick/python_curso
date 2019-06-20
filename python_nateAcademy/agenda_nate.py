import pickle
import os

from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5
ACTION_SHOW_ALL = 6

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT,ACTION_SHOW_ALL]

def print_underlined(param):
    x = len(param)
    print("="*x)
    print(param)
    print("="*x)

def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("\t¿Elige una opcion? ")

    return int(selected_action)


def show_menu():
    os.system("clear")
    print_underlined("Acciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    print("6 - Muestrame todos")
    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts):
    print_underlined("Añadir contacto")
    contact = {
        "name": input("Nombre: "),
        "phone": input("Teléfono: "),
        "email": input("Email: ")
    }
    contacts.append(contact)
    print('Se ha añadido el contacto "{}" correctamente\n'.format(contact["name"]))
    sleep(1)

def show_all(contacts):
    print_underlined("Mostrando contactos")
    for contact in contacts:
        print("Nombre: {}".format(contact["name"]))
        print("Phone: {}".format(contact["phone"]))
        print("Mail: {}".format(contact["email"]))
        print("\n")

def remove_contact(contacts):
    print_underlined("remove_contact")
    search_term = input("Dime que contacto deseas Eliminar ")
    found_contacts = []

    print("He encontrado los siguientes contactos ¿Cual vas a eliminar?:")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) >= 1:
        contact_index = ask_until_option_expected(contact_indexes)
        contacts.pop(contact_index)
        print("Contacto eliminad correctamente")
    elif len(contact_indexes) == 0:
        input("No se ha encontrado ningun contacto.")
        return

    input()


def find_contact(contacts):
    print("\n\nBuscar contacto\n")
    search_term = input("Introducir el nombre del contacto o parte de él: ")
    found_contacts = []

    print("He encontrado los siguientes contactos:")
    contact_indexes = []
    contact_counter = 1

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        return

    print("\nInformación sobre {}\n".format(found_contacts[contact_index]["name"]))
    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
    input()

def export_contacts():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")


def main():
    contacts = load_contacts()
    if not contacts:
        print("La agenda aun no tiene contactos.. (Presione ENTER para continuar ..)", end="")
        input()

    action = show_menu()

    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)
        elif action == ACTION_EXPORT_CONTACT:
            export_contacts()
        elif action == ACTION_SHOW_ALL:
            show_all(contacts)
            input()

        action = show_menu()

    save_contacts(contacts)
    print("¡Adiós!")


if __name__ == "__main__":
    main()
