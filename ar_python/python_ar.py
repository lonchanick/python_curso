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
		#se pueden transformar argumentos a un diccionario de esta forma
		f=open('lab.txt','rb+')
		f.write(b'0123456789abcdef')
		print(f.seek(5))
		print(f.read(1))
		print(f.seek(-3,2))
		print(f.read(1))


def curious_fact_varios():
	#comparacin de secuencias
	#r = (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

	"""
	#Justifica valores con rjust(param)
	for x in range(1, 11):
		print(repr(x).rjust(2), repr(x * x).rjust(3), end='<->')
		# notar el uso de 'end' en la linea anterior
		print(repr(x * x * x).rjust(4))
	
	#otra forma de hacer la misma operacion de arriba
	for x in range(1,11):
		print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
	
	"""
	"""
	#formateo de decimales
	import math
	print("Pi redondeado es: {0:.4f}_".format(math.pi))
	"""

	#formateo de cadenas
	#-> Argumentos nombrados
	def ejercicio_1():
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


	ejercicio_1()

	"""
	print("Esta(e) {objeto} esta {adjetivo}".format(objeto:"casa",adjetivo="Bonita"))
	print("La historia de {0},{1} y {aux}".format(
												  "Ravi",
												  "Zacharias",
												  aux="Pandemonium"))
	"""												  




def main():
	#print(curious_fact_1.__doc__) #muestra el doc de la funcion, si es que lo tiene
	#print(for__.dc_1.__doc__) #muestra la documentacion de una funcion interna
	#For__.dc_5()
	#curious_fact_3()
	#Dict__.dc_1()
	#curious_fact_varios()
	Files__.dc_1()

	pass
	

if __name__ == "__main__":
	main()