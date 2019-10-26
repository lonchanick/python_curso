from ficherosDe_clases.utiles import print_io
import os,time,sys

class Peculiaridades(object):
	"""docstring for Peculiaridades"""
	def sysFunction(self):
		"""demostracion de lo que se puede hacer con la funcion sys.path"""
		def add_new_path():
			print("\n\t¿Quieres agregar una nueva ruta al sys path? [si/no]: ",end="")
			op = input().lower()
			if op == "si":
				print("ok, ingresa el path:",end="")
				path = input().lower()
				print_io("sys.path.insert(0,path)",)
				sys.path.insert(0,path)

				print("Agregando...")
				time.sleep(2)

				os.system("clear")
				print("\tNEW paths:")
				for x in sys.path:
					print_io("",x)

				add_new_path()

			elif op == "no":
				print("\t...Ok hablamos nomas")
			else:
				print("Ingresa una opcion valida")
				add_new_path()

		print("Sys.path: Contine las rutas o directorios donde python busca cada ves que se requiere un import\n  EJEMPLO:")
		print_io("sys.path",)
		for x in sys.path:
			print_io("",x)

		add_new_path()

	def tiposDe_datos():
		os.system("clear")
		num=1
		print_io("num=1 #declaramos un numero")
		print_io("type(num) #averiguamos el tipo de dato que es")
		result=str(type(num))
		print_io("",result)

	def isinstance_funcion():
		os.system("clear")
		result=isinstance(1,int)
		print_io("isinstance(1,int)",result)
		print("="*25)

		string="3.141516"
		result=isinstance(string,str)
		print_io("string=\"3.141516\"")
		print_io("result=isinstance(string,str)")
		print_io("",result)

	def funcion_fracciones():
		os.system("clear")
		import fractions
		print_io("import fractions")
		print_io("x=fractions.Fraction(1,3)")
		x = fractions.Fraction(1,3)
		print_io("x",x)
		print("="*25)

		print_io("x=fractions.Fraction(6,4)")
		x = fractions.Fraction(6,4)
		print_io("x",x)

	def funcion_trigonometria():
		print("En la libreria \"math\" tambien encontraras cosas como la constante pi\ny las funciones trigonometricas sen,cos,tan,etc [p55 Inmersion en python 3...")

	def funcion_listas():
		print("\tObserva como va evolucionado la lista con los diferentes metodos...")
		os.system("clear")
		lista=[100]+[3,14,True]
		inputs=["lista=[100]+[3,14,True]","listas"]
		print_io("","",inputs,lista)
		print("="*25)

		lista.append(False)
		print_io("","",["lista.append(False)","lista"],lista)
		print("="*25)

		lista.extend(["new","elements"])
		aux="lista.extend([\"new\",\"elements\"])"
		print_io("","",[aux,"lista"],lista)
		print("="*25)

		lista.insert(0,"Begining")
		aux="lista.insert(0,\"begin\")"
		print_io("","",[aux,"lista"],lista)
		print("="*25)

		lista.insert(-1,"Before last element")
		aux="lista.insert(-1,\"Before last element\")"
		print_io("","",[aux,"lista"],lista)
		print("="*25)

		print("Vale mencionar que no es lo mismo EXTENDER una lista que agregar al fina APPEND\n")

		newList=['x','Y','Z']
		newList.extend(['extended','elements'])

		inputs=["newList=['x','Y','Z']","newList.extend(['extended','elements'])","newList"]
		print_io("","",inputs,newList)

		newList=['x','Y','Z']
		newList.append(['extended','elements'])

		inputs=["newList=['x','Y','Z']","newList.append(['extended','elements'])"]
		print_io("","",inputs,newList)
		print("="*25)






		
		


