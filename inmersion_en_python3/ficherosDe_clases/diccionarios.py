class Diccionarios(object):
	"""Diccionarios por compresion [3.2] pag 92"""
	def ejemplo_1():
		import os, glob
		metadata = [(item, os.stat(item)) for item in glob.glob('archivos_de_muestra/*copy*.xml')]
		print(metadata [0])

		metadata_dict = {item : os.stat(item) for item in glob.glob('archivos_de_muestra/*copy*.xml')}
		print(type(metadata_dict))
		for x in list(metadata_dict.keys()):
			print(x)

	def diccionario_pc():
			"""diccionario por comprension [3.4] pag 92 """
			import os, glob

			dictt = {os.path.splitext(f)[0]:os.stat(f).st_size for f in glob.glob('archivos_de_muestra/*') if os.stat(f).st_size > 6000}

			print(type(dictt))
			print("Diccionario completo:")
			for key, value in dictt.items():
				print(key, "->",(value/1024),"KB")

			print ("\nClaves del diccionario: \n")
			for x in list(dictt.keys()):
				print (x)

			print("\nDiccionario invertido: ")
			invert = {key : value for value, key in dictt.items()}
			#print(invert)
			for key, value in invert.items():
				print(key, "->",value,"KB")