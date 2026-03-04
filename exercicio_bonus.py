
import os
def clear():
    os.system('cls')


clear()

lista_produtos =[
    {'nome': 'nsx', 'preco': 15000000},
    {'nome': 'rx7', 'preco': 2000000},
    {'nome': 'supra', 'preco': 1200000}
]

produto = {
    'nome':input('nome do produto:'),
    'preco':float(input('Valor do produto:')),
    'quantidade':int(input('Quantidade em estoque:')),
    'categoria':input('Categoria do seu produto:')
}

lista_produtos.append({'nome': produto['nome'], 'preco': produto['preco']})

for lista in lista_produtos:
    print(lista)


'''print(lista_produtos)
print(f'Produto:{produto['nome']}')
print(f'Valor: R${produto['preço']}')'''