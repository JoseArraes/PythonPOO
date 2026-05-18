from rich import print
from rich.panel import Panel


class Churrasco:
    consumo_padrao = 0.400
    preco_kg = 36
    def __init__(self, evento, convidadosn):
        self.convidadosn = int(convidadosn)
        self.evento = evento

    def __str__(self):
        return f"Esse é {self.evento} com {self.convidadosn} pessoas participando"

    def calcular_qtd_carne(self) -> float:
        return self.convidadosn * self.consumo_padrao

    def calcular_qtd_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_qtd_total()/self.convidadosn

    def analisar(self):
        conteudo = f"Analisando [green]{self.evento}[/] com [blue]{self.convidadosn} convidados.[/]"
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao:.3f} Kg e cada Kg custa R${Churrasco.preco_kg:.2f}"
        conteudo += f"\nRecomendo comprar [blue]{self.calcular_qtd_carne():.3f}Kg[/] de carne"
        conteudo += f"\nO custo total será de [green]R${self.calcular_qtd_total():.2f}[/]"
        conteudo += f"\nCada pessoa pagará [yellow]R${self.calcular_custo_individual():.2f}[/] para participar."
        painel = Panel(conteudo, title=self.evento)

        print(painel)

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()

c2 = Churrasco("Fim de ano", 160)
c2.analisar()
