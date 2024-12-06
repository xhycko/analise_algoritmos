# Nome do arquivo de saída
saida = "nomes_aa.csv"

# Ler e imprimir a primeira linha do arquivo
try:
    with open(saida, mode='r', encoding='utf-8') as file:
        primeira_linha = file.readline().strip()
        print(f"Primeira linha do arquivo: {primeira_linha}")
except FileNotFoundError:
    print(f"Arquivo '{saida}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
