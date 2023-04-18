#Para criar uma matriz, usamos numpy.array(forma), em que forma são listas que 
#representam as linhas e colunas.
#NumPy é uma bibliteca muito rica. Veja algumas construções de matrizes usadas em 
#álgebra linear já prontas, com um único comando

import numpy

# Cria matriz 3 x 3 somente com zero
matriz1 = numpy.zeros((3, 3))

# Cria matriz 2 x 2 somente com um
matriz2 = numpy.ones((2,2))

# Cria matriz 4 x 4 identidade #(1 na diagonal principal) usando comandos específicos 
matriz3 = numpy.eye(4) 

# Cria matriz 2 X 5 com números inteiros
#função que gera números inteiros aleatórios. Escolhemos o menor valor como 0 e
#o maior como 100, e também pedimos para serem gerados 10 números. Em seguida, 
#usamos a função reshape() para transformá-los em uma matriz com 2 linhas e 5 colunas. 
matriz4 = numpy.random.randint(low=0, high=100, size=10).reshape(2, 5) 

print('\n numpy.zeros((3, 3)) = \n', matriz1)
print('\n numpy.ones((2,2)) = \n', matriz2)
print('\n numpy.eye(4) = \n', matriz3)
print('\n m4 = \n', matriz4)

print(f"\nSoma dos valores em m4 = {matriz4.sum()}")
print(f"Valor mínimo em m4 = {matriz4.min()}")
print(f"Valor máximo em m4 = {matriz4.max()}")
print(f"Média dos valores em m4 = {matriz4.mean()}")
