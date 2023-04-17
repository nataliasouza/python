#O programa deve receber um salário, com base no valor informado, 
#e algoritmo deve verificar em qual faixa do imposto esse valor se enquadra, 
#quando encontrar a faixa, o programa imprime o valor a ser deduzido. 
#E também já seja impresso o valor do salário com o desconto aplicado.

#Base de cálculo em reais	Alíquota (%)	Parcela a deduzir do IRPF em reais
#Até 1.903,98	-	-
#De 1.903,99 até 2.826,65	7,5	142,80
#De 2.826,66 até 3.751,05	15	354,80
#De 3.751,06 até 4.664,68	22,5	636,13
#Acima de 4.664,68	27,5	869,36

salario = 0
salario = float(input("Digite o salário do colaborador: "))

if salario <= 1903.98:
    print(f"\nO colaborador isento de imposto.")
    print(f"Salário a receber = {salario}")
elif salario <= 2826.65:
    print(f"\nO colaborador deve pagar R$ 142,80 de imposto.")
    print(f"Salário a receber = {salario - 142.80}")
elif salario <= 3751.05:
    print(f"\nO colaborador deve pagar R$ 354,80 de imposto.")
    print(f"Salário a receber = {salario - 354.80}")
elif salario <= 4664.68:
    print(f"\nO colaborador deve pagar R$ 636,13 de imposto.")
    print(f"Salário a receber = {salario - 636.13}")
else:
    print(f"\nO colaborador deve pagar R$ 869,36 de imposto.")
    print(f"Salário a receber = {salario - 869.36}")

