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

class for__(object):
	"""\
	Aqui estan todos los datos curiosos respecto al bucle FOR
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


	def dc_3():
		"""Bucle FOR mas sentencia enumerate"""
		lgdp=["Python","C++","Java",["HTML","CSS","JS"]]
		for i,lg in enumerate(lgdp):
			print(i,lg)

def main():
	#print(curious_fact_1.__doc__) #muestra el doc de la funcion, si es que lo tiene
	#print(for__.dc_1.__doc__) #muestra la documentacion de una funcion interna
	for__.dc_3()

	

	


if __name__ == "__main__":
	main()