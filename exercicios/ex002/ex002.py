class Gafanhoto:
    def __init__(self, n="vazio", i=0):
        self.nome = n
        self.idade = i

    def aniversario (self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome}, idade = {self.idade}"

g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1)
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)
print(g1.__doc__)