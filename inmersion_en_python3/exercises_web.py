def character_input():
	import datetime
	now=datetime.datetime.now()
	name=str(input('Whats your name? '))
	age=int(input('Whats your age? '))
	year_to_calc=50
	year=(year_to_calc-age)+now.year
	print('You will be {} years old in {}'.format(year_to_calc,year))
	pass


def odd_or_even():
	num=int(input('Please type a num: '))
	
	if (num%4)==0:
		print('Is multiple of 4')
	elif (num%2)==0:
		print('Odd')
	else:
		print('Even')

def les_than():
	import random
	num=int(input('Please type a num: '))
	lista=[random.randint(0,101) for item in range(100)]
	#print(lista)
	#lista=
	result = [item for item in lista if item == num]
	print(result)

def divisors():
	num=int(input('Please type a num: '))
	loop=True
	div=2
	result=[]

	while loop:
		if num%div == 0:
			result.append(div)

		div+=1
		if div>num:
			print(result)
			loop=False


