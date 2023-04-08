lista_numeros = [52, 10, 5, 66, 77, 24, 45, 20, 33]

def executar_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
        return False

contem_na_lista = executar_busca_linear(lista_numeros, 20)
    
print(contem_na_lista)
