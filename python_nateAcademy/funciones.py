
"""
def reverse_string(string_to_reverse):
	result =""
	indidex_string_to_reverse = (len(string_to_reverse)-1)

	while indidex_string_to_reverse >= 0:
		result += string_to_reverse[indidex_string_to_reverse]
		indidex_string_to_reverse-=1

	return result

print(reverse_string("hola mundo"))
"""
""""
#encontral el numero mas grande entre 3

def maximo(lista_numeros = []):
	num_max = lista_numeros[0]

	for x in lista_numeros:
		if num_max < x:
			num_max = x

	return num_max

lista = [22,23,11]

print (maximo(lista))

"""
"""
#comprobar si un numero esta dentro de un rango dado

def is_between(num, ran_infe, ran_sup):
	if num >= ran_infe and num <= ran_sup:
		return True
	else:
		return False

print (is_between(101, 5,100))
"""

"""
#funcion que resibe una lista de numeros y devuelve los pares
def pares(lista_numeros = []):
	solo_pares = []
	for x in lista_numeros:
		if x%2 == 0:
			solo_pares.append(x)

	return solo_pares

print(pares([1,2,3,4,5,6,7,8,9,10]))

"""


