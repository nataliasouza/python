#Parâmetro posicional, obrigatório, com valor default, quando a função
# é invocada, caso nenhum valor seja passado, o valor default é utilizado

def calcular_desconto(valor, desconto = 0):
    # O parâmetro desconto possui zero como valor default
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

valor1 = calcular_desconto(100) #Não aplica desconto
valor2 = calcular_desconto(100, 0.25) #Aplica o desconto de 25%

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nPrimeiro valor a ser pago = {valor2}")