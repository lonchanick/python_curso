def curious_fact_1():
	"""\
	Las rebanadas "[:]" sirven para crear una copia
	de la cadena que se esta manipulando
	"""
	lista=[1,8,9,10]

	for n in lista[:]:#genera una copia, de otro modo se hace un bucle infinito
		if(n>8):
			lista.append(n)
		print(lista,end="\n")

def main():
	print(curious_fact_1.__doc__)

if __name__ == "__main__":
	main()