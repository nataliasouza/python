#A função map() é utilizada para aplicar uma determinada função em cada 
#item de um objeto iterável. Para que essa transformação seja feita, a
#função map() exige que sejam passados dois parâmetros: a função e o objeto iterável.

#A função map retorna um objeto iterável. Para que possamos ver o resultado, precisamos 
#transformar esse objeto em uma lista. Ao aplicar o construtor list() para fazer a conversão.

print("Exemplo 1")
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

nova_lista = map(lambda x: x.lower(), linguagens)#o primeiro parâmetro da função map() precisa ser uma função
print(f"A nova lista é = {nova_lista}\n")#A nova lista é = map object at 0x00000237EB0EF320 

nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")#Agora sim, a nova lista é = ['python', 'java', 'javascript', 'c', 'c#', 'c++', 'swift', 'go', 'kotlin']
