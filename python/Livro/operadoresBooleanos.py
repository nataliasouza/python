#Estruturas lógicas em Python: AND, OR, NOT

#Operador booleano AND: Esse operador faz a operação lógica E, ou seja, dada a 
#expressão (a and b), o resultado será True. Quando os dois dos argumentos forem verdadeiros.

#Operador booleano OR: Esse operador faz a operação lógica OU, ou seja, dada a 
#expressão (a or b), o resultado será True. Quando pelo menos um dos argumentos for verdadeiro.

#Operador booleano NOT: Esse operador faz a operação lógica NOT, ou seja, dada a
#expressão (not a), ele inverterá o valor do argumento. se um dos argumentos for verdadeiro, a
#operação o transformará em falso e vice-versa. 

#Livro - Página 24

quantidade_de_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if quantidade_de_faltas <= 5 and media_final >= 7:
    print("\nAluno aprovado!")
else:
    print("\nAluno reprovado!")
