#Crie um dicionário representando um veiculo contendo as chaves "marca", "modelo" e uma lista
#interna chamada "acessorios". Adicione pelo menos 3 acessórios a essa lista utilizando o
#método .append() e imprima o dicionário completo.

corolla = {
    "Marca": "Toyota",
    "Modelo": "Híbrido",
    "Acessorios": []
}

acessorio1 = input("Digite o 1° acessorio: ")
acessorio2 = input("Digite o 2° acessorio: ")
acessorio3 = input("Digite o 3° acessorio: s")

corolla["Acessorios"].append(acessorio1)
corolla["Acessorios"].append(acessorio2)
corolla["Acessorios"].append(acessorio3)

print(corolla)