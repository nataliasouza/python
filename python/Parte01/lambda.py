#Função anônima é uma função que não é construída com o "def" e, por isso,
#não possui nome. Esse tipo de construção é útil, quando a função faz somente
#uma ação e é usada uma única vez. "Expressão Lambda"

somar = lambda x, y: x + y
resultado = somar(x=13, y=33)

print(resultado)