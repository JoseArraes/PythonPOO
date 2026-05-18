from rich import print
from time import sleep
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual=1

        print(f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} paginas.[/] Você está na [yellow]pagina {self.pagina_atual}.[/][/]")

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range (0,qtd,1):
            if not self.fim_do_livro():
                self.pagina_atual+=1
                print(f"Pág{self.pagina_atual}:arrow_forward: ", end=" ")
                sleep(0.5)
                cont +=1
        print(f"[blue]Você avançou {cont} páginas e agora está na [yellow]página {self.pagina_atual}.[/][/]")
        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'.[/]")

    def fim_do_livro(self) -> bool:
        if self.pagina_atual==self.paginas:
            return True
        else:
            return False

l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(80)