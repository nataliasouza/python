#A listcomp é uma forma pythônica de escrever um for.
#E é construída como uma estrutura de decisão (if) a fim de criar um filtro. 
#a variável item será considerada somente se ela tiver "Java" no texto

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
print("Antes da listcomp = ", linguagens)

for i, item in enumerate(linguagens):
    linguagens[i] = item.lower()
    
print("\nDepois da listcomp = ", linguagens)

#construir uma lista que contém somente as linguagens que possuem "Java" no texto

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

#filtro que retorna somente palavras idênticas
linguagens_java = [item for item in linguagens if "Java" in item]

print(f"\n",(linguagens_java))

#Outra forma de construir a lista, porém com muito mais instruções
linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
linguagens_java2 = []

for item in linguagens:
    if "Java" in item:
        linguagens_java2.append(item)

print(f"\n",(linguagens_java2))