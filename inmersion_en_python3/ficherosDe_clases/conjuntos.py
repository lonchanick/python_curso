#from ficherosDe_clases.utiles import print_titulo


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
	def operaciones():
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

		print("Para desclara un cojunto vacio se usa la siguiente notacion")
		print("un_conjunto=set()")

