from ficherosDe_clases.utiles import print_titulo

class Tuplas(object):

	def __init__ (self):
		print_titulo("Operaciones con tuplas")

	def ejemplo_1(self):
		tupla = ("Hola","mundo", 3.1415, "como estas")
		#esto es una tupla; son inmutables 
		print("Ejemplo #1")
		print("Tupla original: ",tupla)
		print("OPERACION #1: v = ('a',2,True)")
		print("OPERACION #2: (x,y,z) = v")
		v = ('a',2,True)
		(x,y,z) = v #Se asigna una tupla a otra como una especie de diccionario
		print("print (x,y,z): ",end="")
		print (x,y,z)

		print("\nEjemplo #2")
		""" se le asigna un numero a cada variable (dias) """
		print("Tupla Original: (LUNES,MARTES,MIERCOLES,JUEVES,VIERNES)")
		print("Operacion: (LUNES,MARTES,MIERCOLES,JUEVES,VIERNES) = range(5)")
		print("print(LUNES,VIERNES,JUEVES) = ",end="")
		(LUNES,MARTES,MIERCOLES,JUEVES,VIERNES) = range(5)
		print(LUNES,VIERNES,JUEVES)