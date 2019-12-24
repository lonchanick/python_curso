def es_diego(param):
	if(param.upper() == "DIEGO"):
		return True
	else:
		return False

def es_kevin(param):
	if(param.upper() == "KEVIN"):
		return True
	else:
		return False

def es_carlos(param):
	if(param.upper() == "CARLOS"):
		return True
	else:
		return False

def es_karla(param):
	if(param.upper() == "KARLA"):
		return True
	else:
		return False

lista=(
	(es_diego,"Este es Diego"),
	(es_kevin,"Este es Diego"),
	(es_carlos,"Este es Carlos"),
	(es_karla,"Esta es Karla")
	)


def main():
	for (fun,cont) in lista:
		if(fun("Diego")):
			print(cont)
	

if __name__ == "__main__":
	main()