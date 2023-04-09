#Estruturas lógicas em Python: AND, OR, NOT

#Operador booleano AND: Esse operador faz a operação lógica E, ou seja, dada a 
#expressão (a and b), o resultado será True. Quando os dois dos argumentos forem verdadeiros.

#Operador booleano OR: Esse operador faz a operação lógica OU, ou seja, dada a 
#expressão (a or b), o resultado será True. Quando pelo menos um dos argumentos for verdadeiro.

#Operador booleano NOT: Esse operador faz a operação lógica NOT, ou seja, dada a
#expressão (not a), ele inverterá o valor do argumento. se um dos argumentos for verdadeiro, a
#operação o transformará em falso e vice-versa. 

#Ordem de precedência: not primeiro, and em seguida e or por último.
#Livro - Página 24

quantidade_de_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if quantidade_de_faltas <= 5 and media_final >= 7:
    print("\nAluno aprovado!")
else:
    print("\nAluno reprovado!")


#Livro - Página 25

A = 15
B = 9
C = 9

print("\n\n---------------------------------------")
print("\nTestando a precedência de AND | OR\n")
print("(B == C or A < B and A < C):")
print(B == C or A < B and A < C)

print("\n((B == C or A < B) and A < C ):")
print((B == C or A < B) and A < C )

