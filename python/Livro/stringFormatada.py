#Modo 1 - usando formatadores de caracteres (igual na linguagem C) para
#imprimir variável e texto

nome = input("Digite um nome: ")
print(f"\nNome digitado: ",nome)

print("\nUsando formatadores de caracteres")
print("Olá %s, bem vindo a disciplina de programação." 
      " Parabéns pelo seu primeiro hello world!" % (nome))

#Modo 2 - usando a função format() para imprimir variável e texto

print("\n\nUsando a função format()")
print("Olá {}, bem vindo a disciplina de programação." 
      " Parabéns pelo seu primeiro hello world!".format(nome))

#Modo 3 - usando strings formatadas

print("\n\nUsando strings formatadas")
print(f"Olá {nome}, bem vindo a disciplina de programação." 
      " Parabéns pelo seu primeiro hello world!"