#função input(), retorna uma string, portanto é preciso converter o resultado,
#da entrada para um tipo numérico, a conversão será usando a função float()

a = 2
b = 0.5
c = 1
x = input("Digite um valor: ")

x = float(x) #Aqui fazemos a conversão da string para o tipo numérico

y = a * x ** 2 + b * x + c

print(f"O resultado de y para x = {x} é {y}")
