#import exercises_web
#exercises_web.character_input()
#exercises_web.odd_or_even()
#exercises_web.les_than()
#exercises_web.divisors() 

#x=tuplas_de_funciones.es_diego("diesgo")
#print(x)


#from ficherosDe_clases import peculiaridades
#peculiaridades.Generadores()

#from ficherosDe_clases.peculiaridades import Excepciones
#Excepciones.exe() # just call the class method

#TRABAJANDO CON CLASES
class Persona():
	"""sirver para comprender la funcionalidades de la clases en python"""
	def __init__(self, n="default_name", e="default_age"):
		self.nombre=n
		self.edad=e

	def infor(self):
		print(self.nombre,self.edad)

	def autoCall(self):
		Persona().infor()
		x=Persona()
		y=Persona("nombre_radical","apellido_radical")
		x.nombre="cambio_radical"
		x.infor()
		y.infor()
		#MUESTRA A LA DOCTSTRING DE LA CLASE A LA QUE PETENECE
		print(y.__doc__)
		#MUESTRA A LA CLASE QUE PERTENECE EL OBJETO INSTANCIADO
		print(y.__class__)


def main():
	Persona().autoCall()
	

if __name__=="__main__":
	main()



