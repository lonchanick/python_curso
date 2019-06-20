from tkinter import *
from tkinter import ttk
import pickle
import os
from time import sleep
from contact import Contact #el nombre de la clase la 1ra con mayuscula

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


def add_contact(contacts,name,phone,email):
    contact = Contact(name,phone,email)
    contacts.append(contact)
    save_contacts(contacts) #|||||||||||||||||||||||||||||||||
    return contact

def add_contact_tk(contacts,name,phone,email, frame_contact_list):

    contact = add_contact(contacts,name,phone,email)
    cols, row = frame_contact_list.grid_size()

    ttk.Label(frame_contact_list, text=contact.name).grid(column=1, row=row, sticky=(W)) #sticky=(W,E)
    ttk.Label(frame_contact_list, text=contact.email).grid(column=2, row=row, sticky=(W)) #sticky=(W,E)
    ttk.Label(frame_contact_list, text=contact.phone).grid(column=3, row=row, sticky=(W)) #sticky=(W,E)

    #Esta es la funcion que carga los contactos ya guardados con pinckle sobre el grid
def load_contacts_grid(contacts,frame_contact_list):

    for contact in contacts:
        cols, row = frame_contact_list.grid_size()
        ttk.Label(frame_contact_list, text=contact.name).grid(column=1, row=row, sticky=(W)) #sticky=(W,E)
        ttk.Label(frame_contact_list, text=contact.email).grid(column=2, row=row, sticky=(W)) #sticky=(W,E)
        ttk.Label(frame_contact_list, text=contact.phone).grid(column=3, row=row, sticky=(W)) #sticky=(W,E)

"""
def ask_new_contact(contacts):
    print_underlined("Añadir contacto")
    contacts = add_contact(contacts, input("Nombre: "),input("Teléfono: "),input("Email: "))
    
    print('Se ha añadido el contacto "{}" correctamente\n'.format(contact["name"]))
    sleep(2)
"""
"""
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
"""
"""
def find_contact(contacts):
    print("\n\nBuscar contacto\n")
    search_term = input("Introducir el nombre del contacto o parte de él: ")
    found_contacts = []

    print("He encontrado los siguientes contactos:")
    contact_indexes = []
    contact_counter = 1

    for contact in contacts:
        if contact.name.find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact.name))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        return

    print("\nInformación sobre {}\n".format(found_contacts[contact_index].name))
    contact = found_contacts[contact_index]
    contact.print_data()
    input()
"""
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
    contacts  = []
    contacts = load_contacts()

    
    
    root = Tk()
    root.title("Agenda con interface")

    

    # frame para AÑADIR contactos =====================
    frame_add_contact = ttk.Frame(root,padding="30 12 30 12")
    frame_add_contact.grid()

        #labels
    ttk.Label(frame_add_contact, text="Nombre").grid(column=1, row=1, sticky=(W)) 
    ttk.Label(frame_add_contact, text="Email").grid(column=2, row=1) #sticky=(W,E)
    ttk.Label(frame_add_contact, text="Telefono").grid(column=3, row=1, sticky=(W)) #sticky=(W,E)

        #entries
    name = StringVar()
    email = StringVar()
    phone = StringVar()


    ttk.Entry(frame_add_contact, width=25, textvariable=name).grid(column=1,row=2)
    ttk.Entry(frame_add_contact, width=30, textvariable=email).grid(column=2,row=2)
    ttk.Entry(frame_add_contact, width=25, textvariable=phone).grid(column=3,row=2)

    
        #button add
    #aqui meto un Label vacio para hacer espacio y se vea mas elegante
    ttk.Label(frame_add_contact, text="").grid(column=1, row=3)
    ttk.Button(frame_add_contact, 
        text="Añadir",
        command=lambda:add_contact_tk(contacts,
            name.get(),
            phone.get(),
            email.get(),
            frame_contact_list)).grid(column=3,row=4,sticky=(S,E))

    # frame para MOSTRAR contactos =====================
    frame_contact_list = ttk.Frame(root,padding="30 12 30 12")
    frame_contact_list.grid()
    load_contacts_grid(contacts,frame_contact_list)
    
    #AQUI EN ADELANTE VAN LOS LABELS PARA MOSTRAR CONTACTOS
        #labels
    ttk.Label(frame_contact_list, text="Nombre", width=25).grid(column=1, row=1) #sticky=(W,E)
    ttk.Label(frame_contact_list, text="Email", width=30).grid(column=2, row=1) #sticky=(W,E)
    ttk.Label(frame_contact_list, text="Telefono", width=25).grid(column=3, row=1) #sticky=(W,E)

    #espacio (FILA) vacio        
    ttk.Label(frame_add_contact, text="").grid(column=1, row=3) 

    #boton salir
    ttk.Button(frame_add_contact,text="Salir",command=root.destroy).grid(column=3,row=4,sticky=(W))

    #Button(root, text="Quit", command=root.destroy).pack()

    root.mainloop()


if __name__ == "__main__":
    main()
