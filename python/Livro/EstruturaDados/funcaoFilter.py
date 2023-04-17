#A função filter() tem as mesmas características da função map(), mas, 
#em vez de usarmos uma função para transformar os valores da lista, nós a usamos para filtrar

#construtor list() para transformá-lo em uma lista com números, que variam de 0 a 20
numeros  = list(range(0, 21))

#criamos uma nova lista com a função filter, que, com a utilização da expressão lambda, retorna somente os valores pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)
