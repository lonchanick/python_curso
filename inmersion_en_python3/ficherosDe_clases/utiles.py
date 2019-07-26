
def print_titulo(titulo):
		size = len(titulo)+2
		print("="*size)
		print("",titulo)
		print("="*size)

def print_sub_titulo(titulo):
		size = len(titulo)+2
		print("",titulo)
		print("-"*size)

def print_io(inputs="", outputs="" ):
		if inputs.strip():
			print("<<",inputs)
		if outputs.strip():
			print(">>",outputs)
