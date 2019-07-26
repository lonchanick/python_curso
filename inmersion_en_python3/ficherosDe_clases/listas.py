from ficherosDe_clases.utiles import print_titulo
from ficherosDe_clases.utiles import print_io #lo q le mandes por parametro lo imprime como entrada y salida de consola .. en ese mismo orden de correspondecia

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
	
	def por_comprension_1(self):
		#PAG 90
		lista = [1,3,5,7]
		[elem * 2 for elem in lista]
		print_io("lista = [1,3,5,7]")
		print_io("[elem * 2 for elem in lista]")
		print(">> ",lista)

	def por_comprension_2(self):
		import os, glob
		print("Busca todos los arvhivos XML en un directorio x y genera la ruta absoluta a cada uno de los mismos.")
		result = [os.path.realpath(item) for item in glob.glob("archivos_de_muestra/*.xml")]
		print_io("result = [os.path.realpath(item) for item in glob.glob(\"archivos_de_muestra/*.xml\")]")
		for x in result:
			print_io("",x)