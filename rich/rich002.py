from rich import print
from rich.panel import Panel

caixa = Panel("Esse aqui é um painel de exemplo", title="Mensagem", style="Blue", border_style="Green", width=20)
print(caixa)