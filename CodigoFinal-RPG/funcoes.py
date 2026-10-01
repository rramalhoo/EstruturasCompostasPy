personagens = []

def criar_personagem():
    nome = input("Digite o nome do personagem: ")
    classe = input("Digite a classe do personagem: ")
    nivel = int(input("Digite o nível do personagem: "))

    personagem = {
        "nome": nome,
        "classe": classe,
        "nivel": nivel,
        "inventario": []
    }

    personagens.append(personagem)



def adicinar_item_inventario():
    nome = input("Digite o nome do personagem: ")

    for personagem in personagens:
        if personagem["nome"] == nome:
            nome_item = input("Digite o item a ser adicionado: ")
            tipo_item = input("Digite o tipo do item (arma, comida, etc.): ")

            item = (nome_item, tipo_item)

            personagem["inventario"].append(item)

            
            print(f"Item '{nome_item}' adicionado ao inventário de {nome}.")
            return

    print(f"Personagem '{nome}' não encontrado.")



def exibir_inventario():
    nome = input("Digite o nome do personagem: ")

    for personagem in personagens:
        if personagem["nome"] == nome:
            if not personagem["inventario"]:
                print(f"O inventário de {nome} está vazio.")
                return
            
            print(f"Inventário de {nome}:")
            for item, tipo in personagem["inventario"]:
                print(f"  - {item[0]} ({tipo[1]})")
            print()
            return

    print(f"Personagem '{nome}' não encontrado.")



def remover_item_inventario():
    nome = input("Digite o nome do personagem: ")

    for personagem in personagens:
        if personagem["nome"] == nome:
            if not personagem["inventario"]:
                print(f"O inventário de {nome} está vazio.")
                return

            
            item_nome = int(input("Digite o número do item a ser removido: ")) - 1

            for item in personagem["inventario"]:
                if item_nome[0] == item_nome:
                    personagem["inventario"].remove(item)
                    print(f"Item '{item[0]}' removido do inventário de {nome}.")
                    return      
                
            print("Número do item inválido.")
            return

    print(f"Personagem '{nome}' não encontrado.")