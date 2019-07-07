class Modulo_os(object):

	def ejemplo_1():
		import os
		dirx = "/home/israel/DEV/python_cursos/inmersion_en_python3/index.py"

		(ruta, fichero) =os.path.split(dirx)
		print("Path: {}\nFichero: {}".format(ruta,fichero))

		(name,exe) = os.path.splitext(fichero) #separando el nombre del fichero de us extencion
		print("File: {}\nExtension: {}".format(name,exe))

	def ejemplo_2():
		"""Listar directorios 3.2.3 [indice del libro]"""
		import os
		import glob
		os.chdir('/home/israel/DEV/python_cursos/inmersion_en_python3/')
		#apunta a esta ruta para hacer importaciones de desde ahi y lo q sea
		result = glob.glob('ejemplos/*.xml')
		#realiza una busqueda dentro de la carpeta ejemplos de todos los documentos terminados en .xml
		print("Busca en: '/directorio_ejemplo' todos los documentos que terminen con .xml = (glob.glob('ejemplos/*.xml'))")
		for x in result:
			print(x)
		print("\n")
		result = glob.glob('ejemplos/*copy*.xml')
		print("Busca en todos los documentos que tienen en su nombre la palabra 'copy' ademas tienen que terminar en .xml")
		for x in result:
			print(x)

	def ejemplo_3():
		""" obtener metadatos de ficheros [3.2.4] pag 88"""
		import os
		import time
		current_dir = os.getcwd() #averigua el directorio actual de trabajo
		print("Directorio actual de trabajo: ",current_dir)
		metadata = os.stat('ejemplos/test_file#1.xml')
		#obtiene los metadatos del archivo test_file#1.xml
		print(metadata.st_mtime)#contiene la fecha y la hora de modificacion pero en un formato que no sirve pa nada (revisar pagina 88 de inmersion a python 3)
		x = time.localtime(metadata.st_mtime) #convierte esos metadatos en algo mas legible
		print("metadatos: ",x)

		print("Tamano del archivo en bytes: ", metadata.st_size)

	def ejemplo_4():
		"""construccion de rutas absolutas"""
		import os
		print("Ruta actual de trabajo: ",os.getcwd())
		print("Ruta absoluta de test_file#1.xml: ",os.path.realpath('archivos_de_muestra/test_file#1.xml'))

	def ejemplo_5():
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

	def ejemplo_6():
		"""diccionarios por compresion"""
		#pendiente 21 / 06 / 2019
		pass