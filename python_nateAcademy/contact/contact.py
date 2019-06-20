import datetime

class Contact(object):
	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email

	def print_data(self):
		print("Nombre {} , Telefono {}, email {}".format(self.name, self.phone, self.email))

	def edad(self):
		birth_date = input("Dime tu fecha de nacimiento [dd/mm/aa] ")
		birth_date = datetime.datetime.strptime(birth_date,"%d/%m/%Y")
		fecha_actual = datetime.datetime.now()
		year_old = fecha_actual - birth_date
		year_old = int(year_old.days/365)
		print("you are {} years old".format(year_old))
		

def main():
	#ni idea porque no me ejecuta este codigo ... chao
	contact = Contact("x","z","y@y.com")
	lista = []
	lista.append(contact)

	contact.name = "111"
	contact.phone = "1111"
	contact.mail = "111"
	lista.append(contact)

	contact.name = "222"
	contact.phone = "222"
	contact.mail = "222"
	lista.append(contact)

	print(lista)


if __name__ == "__main__":
    main()
