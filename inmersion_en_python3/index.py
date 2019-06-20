
#import os #os.system('clear')

def print_titulo(titulo):
	size = len(titulo)+2
	print("="*size)
	print("",titulo)
	print("="*size)

class Listas(object):

	def __init__(self):
		print_titulo("Operaciones con Listas")
			
	def ejemplo_1(self):
		lista = [1,'hola',3.1415,'size'] #lista 1
		otraLista = [1991,'YYY'] #lista 2
		lista+=otraLista[:] #concatena listas
		lista+=[True] #concatena lista
		lista.append(False) #añadir al final
		lista.extend(["size", "End"]) #extiende la lista a varios elementos mas
		lista.insert(0,"Begin") #inserta en a la izquierda de la posicion que se le pase por parametro (el primero)
		lista.append(otraLista) #añade al final pero otra lista
		print("Size: ",len(lista))

		print("LISTA ORIGINAL\n",lista,"\n")

		if lista[-1]:
			print("if outpad -> True")
		else:
			print("if outpad -> False")

		print("lista.count('size'): {}".format(lista.count('size')))
		indice = lista.index('size')
		print("lista.index('size'): {}".format(indice))
		print("lista.index(123): {}".format(lista.index(1991)))
		print("'size' in lista: {}".format('size' in lista))
		del lista[indice]
		print("\n\tdel lista [index of 'size'] \n NUEVA LISTA",lista)
		lista.remove("hola")
		print('\n\tlista.remove("hola") \n NUEVA LISTA:',lista)
		print('\n\tlista.pop(0) = {} \n NUEVA LISTA: {}'.format(lista.pop(0), lista))
		print('\n\tlista.pop() = {} \n NUEVA LISTA: {}'.format(lista.pop(), lista))
		print('\n\tlista.pop() = {} \n NUEVA LISTA: {}'.format(lista.pop(), lista))
		print('\n\tlista.pop() = {} \n NUEVA LISTA: {}'.format(lista.pop(), lista))
		print("\n")
		# tuple() -> resive una lista y la convierte en una tupla
		# list() -> resive una tupla y la convierte en una lista

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


class Conjuntos(object):

	def __init__(self):
		print_titulo("Operaciones con conjuntos")

	def ejemplo_1(self):
		#un_conjunto = {1,11,12,13}
		una_lista = ["hola","mundo",12,13,14,False]
		un_conjunto = set(una_lista)
		print("Conjunto: ",un_conjunto)
		#print("Lista: ",una_lista)
		#conjunto vacio
		conjunto_vacio = set()
		print("\tAgregando '#22' al conjunto -> un_conjunto.add('#22') ")
		un_conjunto.add('#22')
		print("Conjunto: ",un_conjunto)

		print("\tAgregando al conjunto -> un_conjunto.update({'#100', 3.14, 1991, '#22'}) ")
		un_conjunto.update({'#100', 3.14, 1991, '#22'})
		#los elementos repetidos no se agregan
		print("Conjunto: ",un_conjunto)

		print("\tAgregando al conjunto -> un_conjunto.update({99,91},{115,119}) ")
		un_conjunto.update({99,91},{115,119})
		#los elementos repetidos no se agregan
		print("Conjunto: ",un_conjunto)

		print("Agregando al conjunto -> un_conjunto.update([99,91,115,119,'pedo']) ")
		un_conjunto.update([99,91,115,119,'pedo'])
		#los elementos repetidos no se agregan
		print("Conjunto: ",un_conjunto)

		#ELIMINAR ELEMENTOS DE UN CONJUNTO
		#conjunto.discard(): elimina el elemento sin saltar error en caso de no encontrarse
		#	dentro del conjunto en cuestion
		print("un_conjunto.discard('pedo') ")
		un_conjunto.discard('pedo')
		print("Conjunto: ",un_conjunto)

		#conjunto.remove(): a diferencia de discard este en caso de no encontrar el elemento
		#	salta un mensaje de erro
		print("un_conjunto.remove(1991)")
		un_conjunto.remove(1991)
		print("Conjunto: ",un_conjunto)

		#Metodo .pop() tambien diponible
		#Metodo .clear() vacia el conjunto

		#Operaciones entre conjuntos
		""" 
		result = conjunto_1.union(conjunto_2)
		result = conjunto_1.intersection(conjunto_2)
		
		"""
	def operaciones(self):
		comprobador = {1,2,3,4,5,6, 3.1415}
		conjunto_1 = {1,3,5, 3.1415}
		conjunto_2 = {2,4,6, 3.1415}

		print("\tConjunto #1: {} \n\t\tConjunto #2: {} \n".format(conjunto_1,conjunto_2))

		unionResult = conjunto_1.union(conjunto_2)
		print("Union:",unionResult)

		intersectionResult = conjunto_1.intersection(conjunto_2)
		print("Intersection:",intersectionResult)

		difference_Result = conjunto_1.difference(conjunto_2)
		print("Diferencia:",difference_Result, "//CONJUNTO_1 MENOS CONJUNTO_2")

		difference_Result_2 = conjunto_2.difference(conjunto_1)
		print("Diferencia:",difference_Result_2, "//CONJUNTO_2 MENOS CONJUNTO_1")

		symetric_result = conjunto_1.symmetric_difference(conjunto_2)
		#retorna los elementos que son esclusivos de cada conjunto
		print("Diferencia Simetrica:",symetric_result, "//CONJUNTO_1 POR CONJUNTO_2")

		print (conjunto_1.difference(conjunto_2) == conjunto_2.difference(conjunto_1))
		#curiosa operacion de comparacion

		print("*) Consultas a conjuntos") 
		conjunto_3 = {1,3,5}
		conjunto_4 = {1,3,5, 2,4,6}
		print("\tConjunto #3: {} \n\t\tConjunto #4: {} \n".format(conjunto_3,conjunto_4))

		conjunto_3.issubset(conjunto_4)
		print("Conjunto #3 es sub-conjunto de Conjunto #4? ",conjunto_3.issubset(conjunto_4))

		conjunto_4.issuperset(conjunto_3)
		print("Conjunto #4 es super-conjunto de Conjunto #3? ",conjunto_4.issuperset(conjunto_3))

class Diccionario(object):
	"""docstring for diccionario"""
	def __init__(self, arg):
		print("Estamos masomenos claro con el funcionamiento de los diccionarios, eso creo :/ ")

		
		

def main():
	#Conjuntos().operaciones()
	#Listas().ejemplo_1()
	#Tuplas().ejemplo_1() 
	#Os()
	import os
	dirx = "/home/israel/DEV/python_cursos/inmersion_en_python3/index.py"

	(ruta, fichero) =os.path.split(dirx)
	print("Path: {}\nFichero: {}".format(ruta,fichero))

	(name,exe) = os.path.splitext(fichero) #separando el nombre del fichero de us extencion
	print("File: {}\nExtension: {}".format(name,exe)) 

if __name__ == "__main__":
	main()