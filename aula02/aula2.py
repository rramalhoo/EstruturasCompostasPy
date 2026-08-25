# Aula 02 - Estrutura Compostas
# Estrutura usada: Lista de Dicionários

personagens = [
    {"nome": "Arthos", "classe": "Guerreiro", "nivel": 1},
    {"nome": "Luna", "classe": "Maga", "nivel": 2}
]


for personagem in personagens:
    print("Nome:", personagem["nome"])
    print("Classe:", personagem["classe"])
    print("Nível:", personagem["nivel"])
    print()