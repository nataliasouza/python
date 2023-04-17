#As tuplas também são estruturas de dados do grupo de objetos do tipo sequência 
#e são objetos imutáveis.
#Sua utilização ocorre em casos nos quais a ordem dos elementos é importante e 
#não pode ser alterada.

vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

