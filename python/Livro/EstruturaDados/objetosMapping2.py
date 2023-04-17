#Uma única chave em um dicionário pode estar associada a vários valores por meio de
#uma lista, tupla ou até mesmo outro dicionário. Nesse caso, também conseguimos acessar
#os elementos internos. No código a seguir, a função keys() retorna uma lista com todas
#as chaves de um dicionário. A função values() retorna uma lista com todos os valores.
#A função items() retorna uma lista de tuplas, cada uma das quais é um par chave-valor.

#Primeiro, veja que criamos um dicionário em que cada chave está associada
#a uma lista de valores

cadastro = {
            'nome' : ['João', 'Ana', 'Pedro', 'Marcela'],
            'cidade' : ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba'],
            'idade' : [25, 33, 37, 18]
            }

#mostra o tamanho do dicionário
print("len(cadastro) = ", len(cadastro))

#retorna uma lista com todas as chaves no dicionário.
print("\n cadastro.keys() = \n", cadastro.keys())

#retorna uma lista com os valores. Como os valores também são listas, 
#temos uma lista de listas.
print("\n cadastro.values() = \n", cadastro.values())

#retorna uma lista de tuplas, cada uma das quais é composta pela chave e pelo valor.
print("\n cadastro.items() = \n", cadastro.items())

#acessa o valor atribuído à chave 'nome'; nesse caso, uma lista de nomes.
print("\n cadastro['nome'] = ", cadastro['nome'])

#acessa o valor na posição 2 da lista atribuída à chave 'nome'.
print("\n cadastro['nome'][2] = ", cadastro['nome'][2])

#acessa os valores da posição 2 até o final da lista atribuída à chave 'nome'
print("\n cadastro['idade'][2:] = ", cadastro['idade'][2:])


#a função len() retorna quantas chaves um dicionário possui. No entanto,
#e se quiséssemos saber o total de elementos somando quantos há em cada chave? 

print(len(cadastro['nome']))
print(len(cadastro['cidade']))
print(len(cadastro['idade']))

qtde_itens = sum([len(cadastro[chave]) for chave in cadastro])

print(f"\n\nQuantidade de elementos no dicionário = {qtde_itens}")
