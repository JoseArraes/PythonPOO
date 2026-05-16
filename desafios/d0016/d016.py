from rich import print
from rich import inspect

class Funcionario:
    empresa = "Curso em Video"
    def __init__(self, nome, cargo, setor):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f":handshake: Olá sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}"

Funcionario.empresa = "Natura"

c1 = Funcionario("Gustavo", "Diretor", "Administração")
print(c1.apresentar())
c2 = Funcionario("José", "Programador", "TI")
print(c2.apresentar())