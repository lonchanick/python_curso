

# este codio esta incompleto .. este codigo fue el intento por implementar
# clases en el combate pokemos.. decidi bajarme los codigos de Nate y estudiarlos mejor

class Pokemon:
	vida_base = 100
	ataque = 10
	nombre_pokemon ="Pokemon"

	def __init__(self):
		self.vida = vida_base

	def atacar(self, enemigo):
		enemigo.recibir_daño(self.ataque)

	def recibir_daño(self, danio):
		self.vida -= danio

	def mostrat_vida():
		print("Vida de {}: {}".format(self.nombre_pokemon, self.vida))


class Charmander(Pokemon):
	vida_base = 100
	ataque = 10
	nombre_pokemon ="Charmander"


class Pokachu(Pokemon):
	vida_base = 120
	ataque = 10
	nombre_pokemon ="Pikachu"


class bulbasur(Pokemon):
	vida_base = 90
	ataque = 7
	nombre_pokemon ="Bulbasur"




