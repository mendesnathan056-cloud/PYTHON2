from rich.console import Console
from rich.panel import Panel


from carregar_dados  import carregar_dados
from Formatacao_de_dados import Console ,numeros_br 



def mostrar_resultados(df):
    total_registros = len(df)
    total_votos  = df["votos"].sum()
    total_cidade = df["cidade"].nunique()
    total_candidatos = df["candidato"].nunique() 

    texto = f"""
        
        [bold] registros:[/] {numeros_br(total_registros)}\n",
        [bold] votos: [/] {numeros_br(total_votos)}\n",
        [bold] cidade: [/] {numeros_br(total_cidade)}\n",
        [bold] candidatos: [/] {numeros_br(total_candidatos)}" 
      

    """
    Console.print(Panel(texto, title="Eleicoes 2024 (Dados ficticios)", expand=False)) 


if __name__ == "__main__":
    df = carregar_dados()
    mostrar_resultados(df)