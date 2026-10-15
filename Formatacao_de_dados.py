from rich.console import Console

Console = Console()


def numeros_br (valor,casas_decimais=0):
 texto = f"{valor:,.{casas_decimais}f}"
 texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
 return texto
 