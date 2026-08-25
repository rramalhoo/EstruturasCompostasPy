catalogo_filmes = [
    ["Interestelar", "Matrix", "Duna"],                                  # Ficcão
    ["Annabelle", "IT a Coisa", "A Múmia"],                              # Terror
    ["Se Beber, Não Case!", "Gente Grande", "Segurança de Shopping"]    # Comédia
]

print("\nCatálogos de filmes:\n")

print("Ficção:")
for filmes in catalogo_filmes[0]:
    print("-", filmes)


print("\nTerror:")
for filmes in catalogo_filmes[1]:
    print("-", filmes)

print("\nComédia:")
for filmes in catalogo_filmes[2]:
    print("-", filmes)
