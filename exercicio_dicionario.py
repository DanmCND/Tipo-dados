
import os
def clear():
    os.system('cls')



clear()

lista_produtos = []

produto = {
    'nome':input('nome do produto:'),
    'preço':input('Valor do produto:'),
    'quantidade':input('Quantidade em estoque:'),
    'categoria':input('Categoria do seu produto:')
}


print(produto)
print(f'Produto:{produto['nome']}')
print(f'Valor: R${produto['preço']}')
