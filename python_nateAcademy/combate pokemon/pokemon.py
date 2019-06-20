
# este codio esta incompleto .. este codigo fue el intento por implementar
# clases en el combate pokemos.. decidi bajarme los codigos de Nate y estudiarlos mejor


pokemon_elegido = input("Contra que pokemon_elegido quieres pelear? POKE1 / POKE2 / POKE3: ")

vida_picachu = 100
vida_enemigo = 0;

if pokemon_elegido == "POKE1":
	vida_enemigo = 90
elif pokemon_elegido == "POKE2":
	vida_enemigo = 80
elif pokemon_elegido == "POKE3":
	vida_enemigo = 100
else:
	print("Eso no es un pokemon osztia!! ")

while vida_picachu > 0 and vida_enemigo > 0:
	ataque_elegido = input("Que ataque quieres utilizar (chispazo / bola voltio) ?")
	print("\n") 
	
	if ataque_elegido == "chispazo":
		print("Pum 10 puntos de daño para tu enemigo!! ")
		vida_enemigo -= 10

	if ataque_elegido == "bola voltio":
		print("Pum 15 puntos de daño para tu enemigo!! ")
		vida_enemigo -= 15

	

	print("Te quedan",vida_picachu,"de vida!")
	print("La vida de tu enemigo es de: ",vida_enemigo)

	print("\n")
	print("\n")

print("el combate a terminado")

def choose_pokemon():
	chosen_pokemon = input("Elige un pokemon (Bulbasur / Charmander / Pikachu")


def main():
	pokemon = choose_pokemon()

if __name__ == "__main__":
	main()