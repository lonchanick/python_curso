import os

def print_titulo(titulo):
		size = len(titulo)+2
		print("="*size)
		print("",titulo)
		print("="*size)

def print_sub_titulo(titulo):
		size = len(titulo)+2
		print("",titulo)
		print("-"*size)

def print_io(inputs="", outputs="",listasIn=[],listaOuts=[]):
		inputs=str(inputs)
		outputs=str(outputs)

		if inputs.strip():
			print("<<",inputs)

		if outputs.strip():
			print(">>",outputs)

		if listasIn:
			for x in listasIn:
				print("<<",end="")
				print(x)

		if listaOuts:
			print(">>",end="")
			print(listaOuts)

class Menu(object):
	def genMenu(self,opciones=[],title=""):
		os.system("clear")
		if title:
			print("\t",title)
		op=None
		cont = 1
		while op!=0:
			for indice,item in enumerate(opciones):
				aux=indice+1
				print(aux,end="")
				print(")",end="")
				print(item)
			print("0)Salir")
			print("\nSelecciona una opcion: ",end="")
			op=int(input())
			return(op)
		
