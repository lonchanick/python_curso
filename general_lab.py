
def fun_assert(x,y=""):
	"""
	Ejemplo de uso de la funcion assert
	"""
	check=(isinstance(x,int) and isinstance(y,str))
	assert check, "Parametros incorrectos"
	print(x,type(x),y,type(y))

	"""
	formas de obtener la documentacion de la funcion
	1) print(fun_assert.__doc__)
	2) help(fun_assert)
	"""

def f2(self):
	"""
	funcion ejemplo de manejo de archivos
	"""
	file=open("file.txt")
	for x in file:
		print(x.rstrip("\n"))
	file.close()

class Ejem_varios(object):
	"""esta clase es para ejemplificar varios temas de python"""
	def f1(self):
		l=["hola","mundo","como"]
		enum=enumerate(l)
		print(type(enum))
		for i,x in enum:
			print(i,x)

		tupla=(1,2,3)
		print(tupla)

class Ejem_de_def_de_clase(object):
	"""Ejemplo de una clase bien definida"""
	def __str__():
		return "def de clase-> \"lass Ejem_de_def_de_clase(object):\""

class Persona(object):
	"""docstring for Persona"""
	def __init__(self,identificacion,nombre,apellido):
		"""constructor de persona"""
		self.identificacion=identificacion
		self.nombre=nombre
		self.apellido=apellido

	def __str__(self):
		return "{1} {2}, {0}".format(self.identificacion,self.nombre,self.apellido)

class Estudiante(Persona):
	def __init__(self,identificacion,nombre,apellido,nivel):
		Persona.__init__(self,identificacion,nombre,apellido)
		self.nivel=nivel

	def __str__(self):
		return "{} {}, {}, nivel:{}".format(self.identificacion,self.nombre,self.apellido,self.nivel)

def contexto():
	print("vaya mierda")

def lab():
	ob=contexto()


def main():
	cad="Israel"
	if cad:
		print("True")
	else:
		print("False")

if __name__=="__main__":
	main()
