
def imprimir_mensagem(disciplina, curso):
    print(f"Minha primeira função em Python, desenvolvida na disciplina: {disciplina}, do curso: {curso}.")

imprimir_mensagem("Linguagem de Programação", "Desenvolvimento Backend")

#Para que o resultado de uma função possa ser guardado em uma variável, 
#a função precisa ter o comando "return". A instrução "return", 
#retorna um valor de uma função

def imprimir_mensagem(disciplina, curso):
    return f"Minha primeira função em Python, desenvolvida na disciplina: {disciplina}, do curso: {curso}."

result=imprimir_mensagem("Linguagem de Programação", "Desenvolvimento Backend")
print(result)