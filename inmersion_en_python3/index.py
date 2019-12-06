
"""
Es posible importar el fichero, en este caso es 'listas' (que es el nombre del fichero mas no de la funcion) 

from ficherosDe_clases import listas

x = listas.Listas() #hay que instanciar un objeto antes de utilizarlo
	x.ejemplo_1()
"""
import os,time #os.system('clear')
from ficherosDe_clases import utiles
from ficherosDe_clases.utiles import print_titulo
from ficherosDe_clases.listas import Listas
from ficherosDe_clases.tuplas import Tuplas
from ficherosDe_clases.conjuntos import Conjuntos
from ficherosDe_clases.modulo_os import Modulo_os
from ficherosDe_clases.diccionarios import Diccionarios
from ficherosDe_clases.peculiaridades import Peculiaridades
from ficherosDe_clases import excepciones

def menu():

	op=None
	while op!=0:
		os.system("clear")

		mainMenu=utiles.Menu()
		lista=["Excepciones","Tipos de datos","Numeros","Listas"
		,"Tuplas","Conjuntos","Diccionarios","Modulo os","modulo glob"
		,"COSAS INTERESANTES","Ex-Regulares"]
		op=mainMenu.genMenu(lista,"\t\t MENU DE COSILLAS")
	
		if op==1:
			os.system("clear")
			obj=utiles.Menu()
			lista=["ValueError","ImportError"]
			print("Menu de demostracion de errores:")
			value=obj.genMenu(lista)
			if value==1:
				obj=excepciones.Excepciones()
				obj.valueError_funcion()
			elif value==2:
				obj1=excepciones.Excepciones()
				obj1.ImportError_funcion()
		
		elif op==2:
			obj=utiles.Menu()
			lista=["type(param)","isinstance(param,param2)"]
			value=obj.genMenu(lista,"Tipos de Datos: Ejemplos")
			if value==1:
				Peculiaridades.tiposDe_datos()
				input()
			elif value==2:
				Peculiaridades.isinstance_funcion()
				input()

		elif op==3:
			obj=utiles.Menu()
			lista=["Fracciones","Trignonometria"]
			value=obj.genMenu(lista,"Numeros:")
			if value==1:
				Peculiaridades.funcion_fracciones()
				input()
			elif value==2:
				Peculiaridades.funcion_trigonometria()
				input()


		elif op==4:
			obj=utiles.Menu()
			lista=["Metodos de agregado","Busqueda de valores","Eliminar valores"]
			value=obj.genMenu(lista,"Listas de objetos:")
			if value==1:
				Peculiaridades.funcion_listas()
				input()
			elif value==2:
				Peculiaridades.busqueda_de_valores()
				print(Peculiaridades.__doc__)
				input()
			elif value==3:
				Peculiaridades.eliminacion_de_valores()
				input()

		elif op==5:
			obj=Tuplas()
			obj.ejemplo_1()
			input()

		elif op==6:
			obj=Conjuntos()
			obj.ejemplo_1()
			obj.operaciones()
			input()

		elif op==7:
			obj=Diccionarios()
			obj.ejemplo_1()
			obj.diccionario_pc()
			input()

		elif op==8:
			obj=Modulo_os()
			obj.ejemplo_1()
			input()

		elif op==9:
			obj=Modulo_os()
			obj.ejemplo_2()
			obj.ejemplo_3()
			obj.ejemplo_4()
			input()

		elif op==10:
			Peculiaridades.cosas_interesantes()
			input()

		elif op==11:
			Peculiaridades.ex_regulares()
			input()

		elif op==0:
			os.system("clear")
			print("Saliendo...")
			time.sleep(0.4)
			os.system("clear")


def main():
	menu()

	


if __name__ == "__main__":
	main()