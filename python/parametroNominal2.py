#Parâmetro nominal e não obrigatório (kwargs), agora a passagem é feita de modo nominal
#e não posicional, o que nos permite acessar tanto o valor do parâmetro quanto o nome da 
#variável que o armazena.

def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido + {type(kwargs)}\n")
    qtde_parametros = len(kwargs)
    print(f"Quantidade de parâmetros: {qtde_parametros}")

    for chave, valor in kwargs.items():
        print(f"Variável = {chave}, valor = {valor}")

print("\nChamada 1")
imprimir_parametros(estado = "Minas Gerais", idade = 25, nome ="Mallu")

print("\nChamada 2")
imprimir_parametros(desconto=10, valor=100)