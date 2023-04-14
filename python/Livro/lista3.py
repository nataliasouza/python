#Fatiamento(slice) de estruturas sequências
#a lista é um objeto muito versátil, pois sua criação suporta a mistura de vários tipos de dados.

lista = ['Python', 30.61, "Java", 51 , ['a', 'b', 20], "maça"]

print(f"Tamanho da lista = {len(lista)}")

for i, item in enumerate(lista):
    print(f"Posição = {i},\t valor = {item} -----------------> tipo individual = {type(item)}")

print("\nExemplos de slices:\n")

#acessa o valor da posição 1 da lista
print("lista[1] = ", lista[1])

#acessa os valores que estão entre as posições 0 e 2
print("lista[0:2] = ", lista[0:2])

#quando um dos limites não é informado, o interpretador considera o limite máximo
#Como não foi informado o limite inferior, então o slice será dos índices 0 a 2 (2 não incluído)
print("lista[:2] = ", lista[:2])

#acessa os valores que estão entre as posições 3 (incluído) e 5 (não incluído). 
#O limite inferior sempre é incluído.
print("lista[3:5] = ", lista[3:5])

#os indíces da lista variam entre 0 e 5. Quando queremos pegar todos os elementos,
#incluindo o último, devemos fazer o slice com o limite superior do tamanho da lista.
#Nesse caso, é 6, pois o limite superior 6 não será incluído.
print("lista[3:6] = ", lista[3:6])

#outra forma de pegar todos os elementos até o último é não informar o limite superior.
print("lista[3:] = ", lista[3:])

#o slice usando índice negativo é interpretado de trás para frente, ou seja, índice -2 
#quer dizer o penúltimo elemento da lista.
print("lista[-2] = ", lista[-2])

#o índice -1 representa o último elemento da lista
print("lista[-1] = ", lista[-1])

#no índice 5 da lista há uma outra lista, razão pela qual usamos mais um colchete para 
#conseguir acessar um elemento específico dessa lista interna.
print("lista[4][1] = ", lista[4][1])
