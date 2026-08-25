produtos = [
    {"Nome": "Sabonete Dove", "Preço": "R$10", "Quantidade":"25"},
    {"Nome": "Shampoo Pantene", "Preço": "R$40", "Quantidade":"10"},
    {"Nome": "Máscara Capilar", "Preço": "R$35", "Quantidade":"3"}
]

for produto in produtos:
    print("Nome:", produto["Nome"])
    print("Preço:", produto["Preço"])
    print("Quantidade:", produto["Quantidade"])
    print()