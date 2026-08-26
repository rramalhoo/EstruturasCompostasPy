#Crie uma lista de tuplas chamada coordenadas onde cada tupla represente um ponto
#geográfico contendo a latitude e a longitude de uma cidade. Percorra a lista exibindo a latitude e
#a longitude de cada local formatadas adequadamente.

coordenadas = [
    ("Cristo Redentor", "22° 57' 6\" Sul", "43° 12' 39\" Oeste"),
    ("Torre Eiffel", "48° 51' 29\" Norte", "2° 17' 40\" Leste")

]

for local in coordenadas:
    print("Local:", local[0])
    print("Latitude:", local[1])
    print("Longitude:", local[2])
    print()
