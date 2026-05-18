from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def favorito(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: [black on blue]{self.nome}[/]"
        conteudo += f"\nJogos favoritos:"
        for game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: [blue]{game[1]}[/]"
        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        print(painel)

j1 = Gamer("José Augusto", "Redkill02")
j1.favorito("Mario Bros.")
j1.favorito("LOL")
j1.favorito("Fortnite")
j1.ficha()



