#Parâmetro posicional e não obrigatório (args), a passagem de valores é feita
#de modo posicional, porém a quantidade não é conhecida.

def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f"Quantidade de Parametros = {qtde_parametros}")
    
    for i, valor in enumerate(args):        
        print(f"Posição = {i}, valor = {valor}")

print("\nChamada 1")
imprimir_parametros("Minas Gerais", 10, 55.99, "Neuza")

print("\nChamada 2")
imprimir_parametros("SP", "24 horas")