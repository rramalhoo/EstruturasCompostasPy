# Aula 01 - Estrutura Compostas
# Estrutura usada: LISTA DE LISTAS


# Cada lista interna representa uma plataforma de jogos
jogos = [
    ["Minecraft", "Fortnite", "Roblox"],     # Jogos de PC
    ["FIFA", "God of War", "Spider-Man"],    # Jogos de PlayStation 
    ["Mario Kart", "Zelda", "Pokémom"]       # Jogos de Nintendo
]


# Exibindo os jogos por plataforma
print("\nJogos por plataforma:\n")

print("PC:")
for jogo in jogos[0]:
    print("-", jogo)


print("\nPlayStation:")
for jogo in jogos[1]:
    print("-", jogo)

print("\nNintendo:")
for jogo in jogos[2]:
    print("-", jogo)

# Pegar o elemento 1 em cada uma das listas
i=0
while (i<3):
    print(jogos[i] [1])
    i=i+1
    

