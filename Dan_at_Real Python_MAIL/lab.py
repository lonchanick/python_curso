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




def main():
	#Argument_unpacking().exe()
	#Swap_values.exe()

if __name__ == '__main__':
	main()
