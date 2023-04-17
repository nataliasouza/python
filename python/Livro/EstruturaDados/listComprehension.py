#A list comprehension, também chamada de listcomp, é uma forma de criar uma lista
#com base em um objeto iterável. é utilizada quando, dada uma sequência, deseja-se
#criar uma nova sequência, porém com as informações originais transformadas ou
#filtradas por um critério

linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
#A sintaxe comentada abaixo produz o mesmo resultado que a linha 6
#linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split() 

print("Antes da listcomp = ", linguagens)

#Dentro do colchetes há uma variável chamada "item" que representará cada valor da lista original
#Veja que usamos item.lower() for item in linguagens, e o resultado foi guardado dentro da mesma 
#variável original, ou seja, sobrescrevemos o valor de "linguagens"
linguagens = [item.lower() for item in linguagens]

print("\nDepois da listcomp = ", linguagens)

#Antes da listcomp =  ['Python', 'Java', 'JavaScript', 'C', 'C#', 'C++', 'Swift', 'Go', 'Kotlin']

#Depois da listcomp =  ['python', 'java', 'javascript', 'c', 'c#', 'c++', 'swift', 'go', 'kotlin']
