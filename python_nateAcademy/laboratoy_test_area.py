from black_jack_copy import Player

def players_to_play():
		list_players_to_play = []
		cont = 1
		response =""
		name = ""
		
		while response != "N":
			print("Ayudame con tu nombre jugador #{}:".format(cont), end="")
			name = input()
			list_players_to_play.append(Player(name))
			response = input("Deseas agregar mas jugadores (S/N) ?")
			cont+=1

		for x in list_players_to_play:
			print("Jugador: ",x.name)

def main():
	players_to_play()

if __name__ == "__main__":
	main()