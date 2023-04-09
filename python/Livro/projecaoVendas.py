#Criação de um algoritmo que seja capaz de prever quantas peças serão vendidas
#em um determinado mês.
#Se o aumento é constante, podemos usar uma função do primeiro grau para prever
#qual será o resultado em qualquer mês. A função será r = c * mes, onde r é o resultado
#que queremos, c é a contante de crescimento e mes é a variável de entrada.

#Obs.: Optei por nomear as variáveis r = resultado_obtido c = constante_de_crescimento
#mes = vendas_mes

#Exercício 01 - Página 18

constante_de_crescimento = 200 # valor da constante
quantidade_pecas_mes = input("Digite o mês que deseja saber o resultado: ") #função que captura o mês que o cliente digitar
quantidade_pecas_mes = int(quantidade_pecas_mes) #converter para numérico o valor capturado pela função input()

resultado_obtido = constante_de_crescimento * quantidade_pecas_mes #equação do primeiro grau, também chamada função do primeiro grau ou função linear

print(f"\nA quantidade de peças para o mês {quantidade_pecas_mes} será {resultado_obtido}")
