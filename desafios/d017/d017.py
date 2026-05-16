from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
         conteudo = f"{self.nome.center(30,' ')}"
         conteudo += f"{'_'*30}"
         precof = f"{self.valor:,.2f}"
         conteudo += f"{precof.center(30,'~')}"
         etiqueta = Panel(conteudo, title= "Produto", width=34, border_style="bold")
         print(etiqueta)


p1 = Produto("Iphone 17 Pro Max", 25000.85)
p2 = Produto("Notebook Gamer", 8000)

p1.etiqueta()
p2.etiqueta()