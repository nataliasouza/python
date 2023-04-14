frutas = ["maça", "banana", "uva", "mamão", "maça"] #Definição da primeira lista
notas = [8.7, 5.2, 10, 3.5] #Definição da segunda lista

print("maça" in frutas) # True => maça está na lista?
print("abacate" in frutas) # False => abacate está na lista?
print("abacate" not in frutas) # True => abacate não está na lista?
print(min(frutas)) # banana => O mínimo de uma lista de palavras é feito sobre a ordem alfabética. 
print(max(notas)) # 10 => para saber o maior valor de cada lista
print(frutas.count("maça")) # 2 => quantas vezes a palavra "maça" aparece na lista
print(frutas + notas) #concatenação das duas listas 
print(2 * frutas)#multiplicamos por 2 a lista de frutas. É a "cópia" da própria da lista foi criada e adicionada ao final.
