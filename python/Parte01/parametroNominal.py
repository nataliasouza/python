#Parâmetro nominal, obrigatório, sem valor default. Não mais importa a posição
#dos parâmetros, pois eles serão identificados pelo nome, a chamada da função é 
#obrigatório passar todos os valores e sem valor default.

def converter_maiuscula(texto, flag_maiuscula):
    if flag_maiuscula:
        return texto.upper()
    else:
        return texto.lower()

texto = converter_maiuscula(flag_maiuscula=True, texto="joão") #Passagem nominal dos parâmetros.
print(texto)

#Parâmetro nominal, obrigatório, com valor default, nesse grupo os parâmetros podem ou não
#possuir valor default

def converter_minuscula(texto, flag_minuscula=True): # parâmettro flag_minuscula possui o valor default TRUE
    if flag_minuscula:
        return texto.upper()
    else:
        return texto.lower()

texto = converter_minuscula(flag_minuscula=True, texto="LINGUAGEM de programação") 
texto2 = converter_minuscula(texto="Linguagem de programação")
print(texto)
print(texto2)