#documentação completa da biblioteca NumPy está disponível em https://numpy.org/. 
#biblioteca mais poderosa para trabalhar com dados tabulares (matrizes), além de ser
#um recurso essencial para os desenvolvedores científicos, como os que desenvolvem 
#soluções de inteligência artificial para imagens.

#É preciso fazer a instalação com o comando pip install numpy

#toda vez que for usar recusos da biblioteca, é necessário importar 
#a biblioteca para o projeto, como o comando import numpy.

import numpy

matriz_1_1 = numpy.array([1, 2, 3]) # Cria matriz 1 linha e 1 coluna
matriz_2_2 = numpy.array([[1, 2], [3, 4]]) # Cria matriz 2 linhas e 2 colunas
matriz_3_2 = numpy.array([[1, 2], [3, 4], [5, 6]]) # Cria matriz 3 linhas e 2 colunas
matriz_2_3 = numpy.array([[1, 2, 3], [4, 5, 6]]) # Cria matriz 2 linhas e 3 colunas

print(type(matriz_1_1))

print('\n matriz_1_1 = ', matriz_1_1)
print('\n matriz_2_2 = \n', matriz_2_2)
print('\n matriz_3_2 = \n', matriz_3_2)
print('\n matriz_2_3 = \n', matriz_2_3)
