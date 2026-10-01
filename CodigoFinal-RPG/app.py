from funcoes import *

while True:
    print("\n ===Menu de Opções:===")
    print("1. Criar personagem")
    print("2. Adicionar item ao inventário")
    print("3. Exibir inventário")
    print("4. Remover item do inventário")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_personagem()
    elif opcao == "2":
        adicinar_item_inventario()
    elif opcao == "3":
        exibir_inventario()
    elif opcao == "4":
        remover_item_inventario()
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")