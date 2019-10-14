from ficherosDe_clases.utiles import print_io
import os,time

class Peculiaridades(object):
	"""docstring for Peculiaridades"""
	def __init__(self, arg):
		super(Peculiaridades, self).__init__()
		self.arg = arg

	def sysFunction():
		"""demostracion de lo que se puede hacer con la funcion sys.path"""
		def add_new_path():
			print("\n\t¿Quieres agregar una nueva ruta al sys path? [si/no]")
			op = input().lower()
			if op == "si":
				print("ok, ingresa el path:",end="")
				path = input().lower()
				print_io("sys.path.insert(0,path)",)
				sys.path.insert(0,path)

				print("Agregando...")
				time.sleep(2)

				os.system("clear")
				print("\tNEW paths:")
				for x in sys.path:
					print_io("",x)

				add_new_path()

			elif op == "no":
				print("Ok hablamos nomas")
			else:
				print("Ingresa una opcion valida")
				add_new_path()

		import sys
		print("Sys.path: Contine las rutas o directorios donde python busca cada ves que se requiere un import\n  EJEMPLO:")
		print_io("sys.path",)
		for x in sys.path:
			print_io("",x)

		add_new_path()
		


		