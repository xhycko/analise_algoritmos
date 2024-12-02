import random
import csv

primeiros_nomes = [
    "Leonardo", "Isaac", "Galileu", "Marie", "Ada", "Alan", "Albert", "Nikola", 
    "Charles", "Katherine", "Thomas", "Francis", "Alexander", "Johannes", 
    "Stephen", "Carl", "Richard", "Rosalind", "Gregor", "Henrietta", "James", 
    "Erwin", "Niels", "Werner", "Max", "Dmitri", "Emmy", "John", "Barbara", "Grace"
]

nomes_meio = [
    "da Vinci", "Newton", "Galilei", "Curie", "Lovelace", "Turing", "Einstein", 
    "Tesla", "Darwin", "Johnson", "Edison", "Crick", "Bell", "Kepler", "Hawking", 
    "Sagan", "Feynman", "Franklin", "Mendel", "Lacks", "Watson", "Schrödinger", 
    "Bohr", "Heisenberg", "Planck", "Mendeleev", "Noether", "von Neumann", 
    "McClintock", "Hopper"
]

ultimos_nomes = [
    "Smith", "Brown", "Jones", "Garcia", "Martinez", "Lee", "Taylor", "Anderson", 
    "Hernandez", "Moore", "White", "Harris", "Clark", "Lewis", "Robinson", 
    "Walker", "Young", "Allen", "King", "Scott", "Green", "Baker", "Adams", 
    "Nelson", "Hill", "Campbell", "Mitchell", "Roberts", "Carter", "Phillips"
]

saida = "nomes_aa.csv"
numero_nomes = 87951399  # Número total de nomes

def gerar_nome_completo():
    primeiro = random.choice(primeiros_nomes)
    meio = random.choice(nomes_meio)
    ultimo = random.choice(ultimos_nomes)
    idade = random.randint(0, 97)
    peso = round(random.uniform(5, 220), 1)
    return f"{primeiro} {meio} {ultimo};{idade};{peso}"

with open(saida, mode='w', encoding='utf-8') as file:
    print(f"Gerando {numero_nomes} nomes no arquivo {saida}...")
    batch_size = 1000000
    for _ in range(numero_nomes // batch_size):
        batch = [gerar_nome_completo() for _ in range(batch_size)]
        file.write('\n'.join(batch) + '\n')
    resto = numero_nomes % batch_size
    if resto > 0:
        batch = [gerar_nome_completo() for _ in range(resto)]
        file.write('\n'.join(batch) + '\n')

print(f"Arquivo {saida} gerado com sucesso!")
