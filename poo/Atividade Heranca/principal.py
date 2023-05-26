from jogo import Personagem, Jogador

player = (input("Qual é seu personagem? "))

objeto = Personagem(player)

game = (input("Escolha sua classe: Humano, Elfo, Vampiro, Zumbi, Goblin, Demônio, Anões, Guerreiro: ""\n"))
play = Jogador(player, game)

objeto.atacar()

play.usarHabilidade("Ressoância Paralela""\n")

