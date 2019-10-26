import os

class Excepciones(object):
	""" Esto es el famoso doctstring"""

	def valueError_funcion(self):
		print("Si ingresa un numero > 5 se levantar una excepcion de tipo \'ValueError\': ",end="")
		x=int(input())
		if x>5:
			raise ValueError("Si el numero ingresado no es < que 5 entonces se levanta esta excepcion")
		else:
			os.system("clear")
			print("Bien hecho gilipollas")

	def ImportError_funcion(self):
		try:
			import asd
		except ImportError:
			asd=None

		if time:
			print("true")
		else:
			print("false")
		input()
		