from ficherosDe_clases.utiles import print_titulo,print_sub_titulo
"""
print("\n*) COMMAND: DESCRIPTION")
		print("\t<< COMMAND_INPUT")
		print("\t>> {}".format(PARAM))
		print("\t>> {}".format(PARAM))

"""


class Modulo_os(object):

	def ejemplo_1(self):
		import os
		os.system('clear')
		print("\n*) os.getcwd(): Muestra el directorio de trabajo actual")
		print("\t<< os.getcwd()")
		print("\t>>",os.getcwd())
		#directorio += "/ficherosDe_clases" //concatena
		print ("\n*) os.chdir(directorio): Cambia el directorio de trabajo por el asignado por parametro")
		print("\t<< os.path.join(directorio,\"ficherosDe_clases\")")
		print("\t>>",os.path.join(os.getcwd(),"ficherosDe_clases"))

		print("\t<< os.getcwd()")
		print("\t>>",os.getcwd())

		print("\n*) os.path.expanduser('~'): Devuelve la ruta hasta la carpeta del USUARIO actual en el sistema")
		print("\t<< os.getcwd()")
		print("\t>>",os.path.expanduser('~'))

		directorio = os.path.join(os.getcwd(),"archivos_de_muestra/test_file#1.xml")
		(ruta_fich,nombre_fich) = os.path.split(directorio)
		print("\n*) (ruta_fich,nombre_fich) = os.path.split(directorio): Divide la ruta hacia un fichero en: la ruta y el nombre del fichero")
		print("\t<< (ruta_fich,nombre_fich) = os.path.split(directorio)")
		print("\t>> Ruta: {}\n\t>> Nombre: {} ".format(ruta_fich,nombre_fich))

		(nombre,extension) = os.path.splitext(nombre_fich)
		print("\n*) (nombre,extension) = os.path.splitext(nombre_fich): Divide un ficheron en el nombre y la extension")
		print("\t<< (nombre,extension) = os.path.splitext(nombre_fich)")
		print("\t>> Nombre: {}\n\t>> Extension: {} ".format(nombre,extension))
		
		

	def ejemplo_2(self):
		"""Listar directorios 3.2.3 [indice del libro]"""
		import os
		import glob
		os.system('clear')
		print_titulo("MODULO GLOB") 

		result = glob.glob('archivos_de_muestra/*.xml')
		print("\n*) glob.glob('archivos_de_muestra/*.xml'): Obtiene todos los ficheres en el directorio pasado por parametro")
		print("\t<< glob.glob('archivos_de_muestra/*.xml')")
		for item in result:
			print("\t>> {}".format(item))

		#realiza una busqueda dentro de la carpeta ejemplos de todos los documentos terminados en .xml
		result = glob.glob('archivos_de_muestra/*copy*.xml')
		print("\n*) glob.glob('archivos_de_muestra/*.xml')): \n  Busca en: '/archivos_de_muestra' todos los documentos que terminen con .xml")
		print("\t<< glob.glob('archivos_de_muestra/*.xml')")
		for item in result:
			print("\t>> {}".format(item))


	def ejemplo_3(self):
		print_titulo("OBTENER METADATOS DE FICHEROS") 
		""" obtener metadatos de ficheros [3.2.4] pag 88"""
		import os
		import time
		metadata = os.stat('archivos_de_muestra/test_file#1.xml')
		#obtiene los metadatos del archivo test_file#1.xml
		#metadata.st_mtime#contiene la fecha y la hora de modificacion pero en un formato que no sirve pa nada (revisar pagina 88 de inmersion a python 3)
		x = time.localtime(metadata.st_mtime) 
		#convierte la fecha obtenida en algo mas legible
		print("\n*) Obtiene los metadatos del archivo test_file#1.xml")
		print("\t<< os.stat('archivos_de_muestra/test_file#1.xml')")
		print("\t>> {}".format(metadata))

		print("\n*) Combierte en un formato mas legible lo obtenido en la linea anterior")
		print("\t<< time.localtime(metadata.st_mtime)")
		print("\t>> {}".format(x))

		print("\n*) Devuelve el tamaño del arvhivo")
		print("\t<< metadata.st_size")
		print("\t>> {}".format(metadata.st_size))

	def ejemplo_4(self):
		"""construccion de rutas absolutas PAG 89"""
		print_titulo("CONSTRUCCION DE RUTAS ABSOLUTAS") 
		import os
		print("\n*) Ruta absoluta de test_file#1.xml")
		print("\t<< os.path.realpath('archivos_de_muestra/test_file#1.xml')")
		print("\t>> {}".format(os.path.realpath('archivos_de_muestra/test_file#1.xml')))

	def ejemplo_5(self):
		"""listas por compresion [3.3] pag 89"""
		una_lista = [1,3,5,9]
		print("Lista original: ", una_lista)
		una_lista = [elem * 2 for elem in una_lista]
		print("Pos compresion: ", una_lista)

		print("="*95)
		print("DEVUELVE LA RUTA ABSOLUTA DE TODOS LOS ARVHIVOS QUE ESTAN EN LA CARPETA archivos_de_muestra")
		import os,glob
		archivos = glob.glob("archivos_de_muestra/*.xml")
		rutas_archivos = [os.path.realpath(item) for item in archivos]
		for x in rutas_archivos:
			print(x)

		bytes_var = 6000 #numero de bytes para filtrar
		print("="*95)
		print("FILTRE LOS ARCHIVOS MAYORES A {} BYTES".format(bytes_var))
		results = [item for item in glob.glob('archivos_de_muestra/*.xml') if os.stat(item).st_size > bytes_var]
		for x in results:
			byte_size = os.stat(x).st_size
			kb = byte_size/1024
			print(x," ->{} BYTES ->{} KB".format(byte_size,kb))

	def ejemplo_6(self):
		"""diccionarios por compresion"""
		#pendiente 21 / 06 / 2019
		pass