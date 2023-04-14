#Operações em comum dos objetos do tipo sequência

texto = "Aprendendo Python na disciplina de linguagem de programação."

print(f"{texto}")
print(f"Tamanho do texto = {len(texto)}") #permite saber o tamanho da sequência
print(f"Python in texto = {'Python' in texto}")#permite saber se um determinado valor está ou não na sequência
print(f"Quantidade de y no texto = {texto.count('y')}")#permite contar a quantidade de ocorrências de um valor
print(f"As 5 primeiras letras são: {texto[0:6]}")#notação com colchetes permite fatiar a sequência, exibindo somente partes dela. 

