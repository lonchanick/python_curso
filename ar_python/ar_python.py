#DC:significa dato curioso

import random


def curious_fact_1():
	"""\
	Las rebanadas "[:]" sirven para crear una copia
	de la cadena que se esta manipulando
	"""
	lista=[1,8,9,10]

	for n in lista[:]:#genera una copia, de otro modo se hace un bucle infinito
		if(n>8):
			lista.append(n)
		print(lista,end="\n")

def curious_fact_2():
	"""/
	lambdas: son funciones anonimas, practicas (hasta ahora)
	"""
	yoin = lambda sep,cad : sep.join(cad) #declaracion de la funcion lambda

	x=yoin('/',["home","israel","DEV"]) #mandando parametros a la funcion
	print(x)

def curious_fact_3():
	"""/
	desempaquetando argumentos o parametros en una funcion
	Argumentos nombrados
	"""
	def funtion_1(nombre,apellido,ci):
		print("Hola {} {}, tu CI es: {}".format(nombre,apellido,ci))

	arg_1=["Diego","Israel", 91991]
	arg_2={"nombre":"Jhon","apellido":"Alejandro","ci":"091230"}
	funtion_1(*arg_1)
	funtion_1(**arg_2)

class For__(object):
	"""\
	Aqui estan todos los datos curiosos respecto al bucle FOR
	DC = Dato Curioso
	"""
	def dc_1():
		"""DC: for con incremento diferente de 1 (lo usual) """
		lst=[x for x in range(1,11)]
		print(lst)
		for x in range(0,10,2): #solo imprime los indices pares de la lista
			print("lst[",x,"]=",lst[x])

	def dc_2():
		"""bucle FOR con sentencia else"""
		lst=[random.randint(1,10) for x in range(0,10)]
		print(lst)
		r=int(input("Ingresa un numero gilipollas: "))
		print("has ingresado",r)
		for x in range(len(lst)):
			if r == lst[x]:
				print("si se encuentra en la lista")
				break
		else:
			print("no esta en la lista")
	
	def dc_3():
		"""bucle FOR mas sentencia "continue"
		"""
		for num in range(2, 10):
		     if num % 2 == 0:
		         print("Encontré un número par", num)
		         continue
		     print("Encontré un número", num)


	def dc_4():
		"""Bucle FOR mas sentencia enumerate"""
		lgdp=["Python","C++","Java",["HTML","CSS","JS"]]
		for i,lg in enumerate(lgdp):
			print(i,lg)

	def dc_5():
		"""\
		Este ejercicio muestra la complejidad de las listas por compresion
		anidadas, cada funcion estas mas simplificada que la otra pero todas
		hacen el mismo trabajo (calcular la traspuesta de una matriz)
		"""
		def traspuesta_metodo_1(vec):
			traspuesta = []

			for i in range(3):
				fila_traspuesta = []
				for fila in vec:
					fila_traspuesta.append(fila[i])

				traspuesta.append(fila_traspuesta)

			return (traspuesta)

		def traspuesta_metodo_2(vec):
			trs = []
			for i in range(3):
				trs.append([x[i] for x in vec])
			return trs

		def traspuesta_metodo_3(vec):
			traspuesta = []
			traspuesta = [[fila[x]  for fila in vec] for x in range(3)]
			return (traspuesta)

		vec = [[1,2,3], [4,5,6], [7,8,9]]
		print(traspuesta_metodo_1(vec))
		print(traspuesta_metodo_2(vec))
		print(traspuesta_metodo_3(vec))

class Dict__(object):
	"""/
	Aqui estan todos los datos curiosos respecto al los diccionarios
	DC = Dato Curioso
	"""
	def dc_1():
		#se pueden transformar argumentos a un diccionario de esta forma
		d = dict(sape=4139, guido=4127, jack=4098)
		print(d)

class Files__(object):
	"""/
	trabajando con archivos
	DC = Dato Curioso
	"""
	def dc_1():
		#manipuladno un ficheron con seek y read
		f=open('lab.txt','rb+')
		f.write(b'0123456789abcdef')
		print(f.seek(5))
		print(f.read(1))
		print(f.seek(-3,2))
		print(f.read(1))

	def dc_2():
		#Abre un archivo
		with open('credo.txt') as f:
				file=list(f)
				print(file[0])

	def dc_3():
		#Todo archivo abierto tiene un puntero que puede ser manipulado con las funciones
		#seek y tell
		with open('credo.txt') as f:
			print(f.tell())#Nos dice donde esta el puntero para manipular el archivo
			print(f.readline())#Muestra la linea completa
			f.seek(22)#Mueve el puntero al elemento 22 (Cuidado cuando sea un file binario)
			print(f.tell())#Nos indica la posicion actual del puntero
			print(f.readline())#Muestra segun a donde este apuntando el puntero

			"""
			#esto deberia funcionar solo con archivos binarios no con tipo texto
			#El puntero puede ser desplazado desde una "posicion relativa"
			# 1 -> indica que la posicion "relativa" será la posicion "actual" del puntero
			# 2 -> indice que la posición relativa será el fin del archivo
			# 0 -> indica el inicio del archivo, por defecto esta es dejada si el campo esta vacio

			f.seek(26,1)
			print(f.readline())
			"""

		
class curious_fact_varios(object):

	def ejemplo_2():
		#comparacin de secuencias
		r = (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
		print(r)

	def ejemplo_3():
		#Justifica valores con rjust(param)
		for x in range(1, 11):
			print(repr(x).rjust(2), repr(x * x).rjust(3), end='<->')
			# notar el uso de 'end' en la linea anterior
			print(repr(x * x * x).rjust(4))
		
		#otra forma de hacer la misma operacion de arriba
		print('\notra forma de hacer la misma operacion de arriba')
		for x in range(1,11):
			print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
		
	def ejemplo_4():
		#formateo de decimales
		import math
		print("Pi redondeado es: {0:.4f}_".format(math.pi))

	def ejemplo_1():
	#-> Argumentos nombrados
	#formateo de cadenas
		d={
			'lunes':1,
			'martes':2,
			'miercoles______ex':3,
			'jueves':4,
			'viernes':5,
			'sabado________ex':6,
			'domingo____ex':7
		}

		for k,v in d.items():
			if(len(k)>9):
				k=k[0:9]
			print('{0:9} <==> {1}'.format(k,v))

		r=vars()
		print(r)

	def ejemplo_5():
		#Mas ejemplos de formateo de cadenas
		print("Esta(e) {objeto} esta {adjetivo}".format(objeto="casa",adjetivo="Bonita"))
		print("La historia de {0},{1} y {aux}".format(
												  "Ravi",
												  "Zacharias",
												  aux="Pandemonium"))

def main():
	#print(curious_fact_1.__doc__) #muestra el doc de la funcion, si es que lo tiene
	#print(for__.dc_1.__doc__) #muestra la documentacion de una funcion interna
	#For__.dc_5()
	#curious_fact_3()
	#Dict__.dc_1()
	#curious_fact_varios.ejemplo_3()
	#Files__.dc_1()
	def f(uno,dos,tres,cuatro):
		print("{}-{}-{}-{}".format(uno,dos,tres,cuatro))

	args={'cuatro':4,'dos':2,'uno':1,'tres':3}
	l=[value for key,value in args.items()]
	t=tuple(l)	

	f(*t)

if __name__ == "__main__":
	main()