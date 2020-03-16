import time,os,random

def visaje():
	#esta wea no sirve
	for x in range(0,3):
		print(".",end="")
		time.sleep(0.3)


def character_input():
	import datetime
	now=datetime.datetime.now()
	name=str(input('Whats your name? '))
	age=int(input('Whats your age? '))
	year_to_calc=50
	year=(year_to_calc-age)+now.year
	print('You will be {} years old in {}'.format(year_to_calc,year))
	pass


def odd_or_even():
	num=int(input('Please type a num: '))
	
	if (num%4)==0:
		print('Is multiple of 4')
	elif (num%2)==0:
		print('Odd')
	else:
		print('Even')

def les_than():
	import random
	num=int(input('Please type a num: '))
	lista=[random.randint(0,101) for item in range(100)]
	#print(lista)
	#lista=
	result = [item for item in lista if item == num]
	print(result)

def divisors():
	num=int(input('Please type a num: '))
	loop=True
	div=2
	result=[]

	while loop:
		if num%div == 0:
			result.append(div)

		div+=1
		if div>num:
			print(result)
			loop=False

def ListOverlap():
	"""
	esta funcion saca solo los elementos que se contienen en amabas listas
	"""
	"""
	import random
	a = [random.randint(0,101) for item in range(50)]
	b = [random.randint(0,101) for item in range(50)]
	result=(set(a).intersection(set(b)))
	print(result)
	"""

	"""
	esta funcion saca solo los elementos que se contienen en amabas listas
	"""
	import random
	result=[]
	a = [random.randint(0,101) for item in range(10)]
	b = [random.randint(0,101) for item in range(10)]
	print(a,"\n",b)

	result=[item for item in a if item in b]
	print(result)


def palindromo(param):
		if len(param)<1:
			return("palabra no valida")
		else:
			rev=''.join(reversed(param))
			if(rev != param):
				print(rev," != ", param)
				return "No es palindromo"
			else:
				print(rev," == ", param)
				return "Si es palindromo"


#EXERCISE 7: LIST COMPRENHENSIONS
def exercise7():
	import random
	lista=[random.randint(0,101) for x in range(10)]
	print("before",lista)
	r=[x for x in lista if x%2 == 0]
	print("after",r)

def exercise8():
	pass

def exercise9():
	tryed=0
	num=random.randint(0,10)

	while True:
		tryed+=1
		iu=int(input("Guess the number: "))
		print(num)
		if iu==num:
			os.system('clear')
			print("Right! You win!")
			print("Attempts number: {}".format(tryed),end="")
			op=str(input("\nSalir [x] Keep playing [p]: "))
			if op=='x':
				break
			elif op=='p':
				os.system('clear')
				exercise9()
		elif(iu<num):
			print("Too low! Try again")
		else:
			print("Too hight! Try again")

def exercise10():
	#Primero se genera un tipo de lista con tamaño y elementos aleatorios
	#Luego se genera una lista de listas del tipo antes mencionado
	listas=[[],[]]
	listas[0]=[random.randint(0,101) for x in range(random.randint(5,14))]
	listas[1]=[random.randint(0,101) for x in range(random.randint(5,14))]

	print("   Figure out commons elements")
	
	#imprime el tamano y el contenido
	for x in listas:
		print("Size: {} Content: {}".format(len(x),x))

	#genera he imprime los elementos comunes en cada lista
	x=set(listas[0])
	y=set(listas[1])
	r=x.intersection(y)
	r=list(r)
	print("Resultado: ",r)

def exercise11():
	pass

def exercise12():
	lista=[random.randint(0,101) for x in range(10)]
	new_list=[]
	new_list.append(lista[0])
	new_list.append(lista[len(lista)-1])
	print("Lista actual",lista)
	print("Nueva lista",new_list)


def exercise13():
	"""Esta funcion de fibonacci esta mal (no se que es fibonacci, chao"""
	x=int(input("How many numbers would you like?"))
	a,b=0,1
	for i in range(x):
		print(a+b)
		a=b
		b=b+1
		

def exercise14(param):
	if param==1:
		'''
		esta solucion emplea conjuntos
		los conjuntos no contienen elementos repetidos
		'''
		lista=[random.randint(0,101) for x in range(20)]
		print("lista:",lista)
		print("conjunto",set(lista))
		#from inmersion_en_python3.ficherosDe_clases.conjuntos import Conjuntos
		#Conjuntos.operaciones()
	elif param==2:
		"""solucion dos"""
		lista=[random.randint(0,101) for x in range(20)]
		print("lista: ",lista)

		contenedor=[]
		duplicados=[]

		for x in lista:
			if x not in contenedor:
				contenedor.append(x)
			else:
				duplicados.append(x)

		print("resul: ",contenedor)
		print("duplicados: ",duplicados)
	else:
		print("La solucion que has pedido no exite mira el numero que pasaste como parametro")

def main():
	#exercise9()
	#visaje()
	#exercise13()
	exercise14(1)


if __name__ == "__main__":
	main()