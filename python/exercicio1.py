a = 2 
b = 1

equacao = input("Digite a formula geral da equaçao linear: ")
print(f"\nA entrada do usuário {equacao} é do tipo{type(equacao)}")

for x in range(5):
    resultado = eval(equacao)
    print(f"\nResultado da equação para x = na posição {x} é {resultado}")