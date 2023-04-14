#Exercício de análise de texto, dado um texto sobre strings em Python, 
#queremos saber quantas vezes o autor menciona a palavra string ou strings. 

texto = """\nOperadores de String
Python oferece operadores para processar texto (ou seja, valores de string).
Assim como os números, as strings podem ser comparadas usando operadores de comparação:
==, !=, <, > e assim por diante.
O operador ==, por exemplo, retorna True se as strings nos dois lados do operador tiverem o mesmo valor (Perkovic, p. 23, 2016).
"""
print(texto)

texto = texto.lower()
texto = texto.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace("\n", " ")

print(f"Texto utilizando replace():\n", (texto))

print(f"\nTamanho do texto = {len(texto)}")
lista_palavras = texto.split()

print(f"\nAs 10 primeiras palavras do texto = ",(lista_palavras[:10]))

print(f"\nTamanho da lista de palavras = {len(lista_palavras)}")

total = lista_palavras.count("string") + lista_palavras.count("strings")

print(f"\nQuantidade de vezes que string ou strings aparecem = {total}")
