#Percorre os elementos da sequência procurando aquele de destino, começa por uma das 
#extremidades da sequência e vai percorrendo até encontrar (ou não) o valor desejado.

#vamos precisar de uma estrutura de repetição (for) para percorrer a sequência, e uma estrutura
#de decisão (if) para verificar se o valor em uma determinada posição é o que procuramos. 

#recebe uma lista e um valor a ser localizado
def executar_busca_linear(lista, valor):
    #A estrutura de repetição, percorrerá cada elemento da lista pela comparação com o
    #valor buscado.Caso este seja localizado, então a função retorna o valor booleano True; 
    #caso não seja encontrado, então retorna False.
    for elemento in lista:
        if valor == elemento:
            print("TRUE")
            return True
    print("FALSE")
    return False

import random

#uma lista de 50 valores com números inteiros randômicos que variam entre 0 e 1000.
lista = random.sample(range(1000), 50)

#A sorted()função retorna uma lista classificada do objeto iterável especificado.
# Você pode especificar a ordem crescente ou decrescente. As strings são classificadas alfabeticamente
#e os números são classificados numericamente.
print(sorted(lista))

executar_busca_linear(lista, 10)
