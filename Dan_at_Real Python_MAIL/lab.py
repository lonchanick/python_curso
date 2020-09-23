class Argument_unpacking(object):
	'''Funcion para desempaquetar argumentos coño cuantas veces te lo digo?'''
	def funct(self,nombre,edad,direccion):
		print("{}".format(nombre))
		print("{}".format(edad))
		print("{}".format(direccion))

	def exe(self):
		t=("Israel",22,"las palmas")
		print("Desempaquetado #1:\n")
		self.funct(*t)
		d={
		"nombre":"Israel",
		"edad":22,
		"direccion":"Las palmas",
		}
		print("\nDesempaquetado #2:\n")
		self.funct(**d)
	
	def __str__(self):
		return "Desempaquetado de argumentos"

class Swap_values(object):
	'''como intercambiar valores de manera practica'''
	def exe():
		a=100
		b=500

		#common way		
		temp=a
		a=b
		b=temp
		print("Common way: ",a,b)

		#short-hand way
		a=100
		b=500
		a,b=b,a
		print("Short-hand way: ",a,b)

class IsVSdoubleEqual(object):
	def exe():
		a=[1,2,3]
		b=a

		print(repr('a=[1,2,3]'))
		print(repr('b=a'))
		print('<<<a is b')
		print('>>>',a is b)
		print('<<<a == b')
		print('>>>',a == b)

		print('\n')
		c=list(a)
		print(repr('c=list(a)'))
		print('<<<a is c')
		print('>>>',a is c)
		print('<<<a == c')
		print('>>>',a == c)
		print()
		print(repr('DATA:"is" expressions evaluate to True if two variables point to the same object "==" evaluates to True if the objects referred to by the variables are equal'))
		
class FirstClassCitizen(object):
	# Functions are first-class citizens in Python:
	# They can be passed as arguments to other functions,
	# returned as values from other functions, and
	# assigned to variables and stored in data structures.
	
	def suma(x,y):
		return x+y

	print('def suma(self,x,y):\n\treturn x+y')
	print()
	l=[suma]
	print('<<<',end='')
	print(repr('l=[suma]'))
	print('>>>',l[0])
	print('>>>l[0](10,19)')
	r=l[0](10,19)
	print('>>>',r)


def main():
	#Argument_unpacking().exe()
	#Swap_values.exe()
	#IsVSdoubleEqual.exe()
	FirstClassCitizen()

if __name__ == '__main__':
	main()
