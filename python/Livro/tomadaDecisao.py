#A construção do if(se)deve ser feita com dois pontos ao final da instrução e
#e deve possuir uma identação específica de uma tabulação ou 4 espaços em branco.

#Estrutura condicional simples

a = 5
b = 10

if a < b:
    print("\na é menor do que b")
    r = a + b
    print(r)


#Estrutura condicional composta

a = 10
b = 5

if a < b:
    print("\na é menor do que b")
    r = a + b
    print(r)
else:
    print("\na é maior do que b")
    r = a - b
    print(r)

#Estrutura condicional

cod_compra = 5111

if cod_compra == 5222:
    print("\nCompra à vista.")

elif cod_compra == 5333:
    print("\nCompra no boleto.")

elif cod_compra == 5444:
    print("\nCompra no cartão.")

else: print("\nCódigo não cadastrado")