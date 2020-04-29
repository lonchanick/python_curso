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

class for__(object):
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



def main():
	#print(curious_fact_1.__doc__) #muestra el doc de la funcion, si es que lo tiene
	#print(for__.dc_1.__doc__) #muestra la documentacion de una funcion interna
	#for__.dc_5()
	#curious_fact_3()



	l = [1,2,3,4,5,6]
	del l[1:4]
	print(l)

if __name__ == "__main__":
	main()