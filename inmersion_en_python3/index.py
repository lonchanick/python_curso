
#import os #os.system('clear')
from ficherosDe_clases.utiles import print_titulo
from ficherosDe_clases.listas import Listas
"""
Es posible importar el fichero, en este caso es 'listas' (que es el nombre del fichero mas no de la funcion) 

from ficherosDe_clases import listas

x = listas.Listas() #hay que instanciar un objeto antes de utilizarlo
	x.ejemplo_1()
"""
from ficherosDe_clases.tuplas import Tuplas
from ficherosDe_clases.conjuntos import Conjuntos
from ficherosDe_clases.modulo_os import Modulo_os
from ficherosDe_clases.diccionarios import Diccionarios
from ficherosDe_clases.diccionarios import Diccionarios
from ficherosDe_clases.peculiaridades import Peculiaridades

def main():

	#Me quede en indentar codigo .. pag 41
	Peculiaridades.sysFunction()#print(Peculiaridades.sysFunction.__doc__)
	#Listas().ejemplo_1()
	#Listas().por_comprension_1()
	#Listas().por_comprension_2()
	#Tuplas().ejemplo_1()
	#Conjuntos().ejemplo_1()
	#Modulo_os.ejemplo_5()
	#print(Modulo_os.ejemplo_4())
	#Diccionarios.ejemplo_1()
	#Diccionarios.diccionario_pc()

	pass


if __name__ == "__main__":
	main()