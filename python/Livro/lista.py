#Lista é uma estrutura de dados do tipo sequencial que possui 
#como principal característica ser mutável. Ou seja, novos valores 
#podem ser adicionados ou removidos da sequência. Em Python, as 
#listas podem ser construídas de várias maneiras:

# Usando um par de colchetes para denotar uma lista vazia: lista1 = []
# Usando um par de colchetes e elementos separados por vírgulas: lista2 = ['a', 'b', 'c']
# Usando uma "list comprehension": [x for x in iterable]
# Usando o construtor de tipo: list()

vogais = ['a', 'e', 'i', 'o', 'u'] # também poderia ter sido criada usando aspas duplas
print(f"\nTipo do objeto vogais = {type(vogais)}")

for vogal in vogais:
    print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')


#Mesmo resultado, mas utilizando a função append().
#função append(), que adiciona um novo valor ao final da lista. 
#Na sintaxe usamos vogais.append(valor), notação que significa que a 
# função append() é do objeto lista. 

print(f"\n\nExemplo 2:\n")

vogais = []
print(f"Tipo do objeto vogais = {type(vogais)}")

vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

for posicao, valor_da_letra in enumerate(vogais): #função enumerate(), usada p/ percorrer um objeto iterável retornando a posição e o valor
    print(f"Posição = {posicao}, valor = {valor_da_letra}")


