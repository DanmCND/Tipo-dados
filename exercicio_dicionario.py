'''
🔧 O que você deve fazer

Criar um dicionário chamado produto contendo as seguintes informações:

nome do produto
preço
quantidade em estoque
categoria

Depois disso o programa deve:

Mostrar todas as informações do produto
Mostrar apenas o nome do produto
Mostrar apenas o preço do produto

DICA IMPORTANTE
Para pegar o valor de uma chave:

NOME_DA_VARIAVEL["NOME_DA_CHAVE"]
Isso retorna o valor que colocamos na chave.

✅ Critérios para a atividade estar correta
Criar um dicionário
Utilizar pelo menos 4 chaves
Acessar valores do dicionário
 
⭐ Desafio extra (opcional)
 
Criar uma lista de produtos, onde cada produto é um dicionário e incrementar a lista.
 
Exemplo:
produtos = [
    {"nome": "Mouse", "preco": 150},
    {"nome": "Teclado", "preco": 200},
    {"nome": "Monitor", "preco": 1200}
]
 
Mostrar todos os produtos utilizando um for.


'''
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
