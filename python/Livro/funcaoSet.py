#Um objeto do tipo set habilita operações matemáticas de conjuntos, tais como: 
#união, intersecção, diferenteça, etc. 

#Para construir com utilização da função set(iterable), obrigatoriamente temos 
#de passar um objeto iterável para ser transformado em conjunto. 
#Esse objeto pode ser uma lista, uma tupla ou até mesmo uma string 

vogais_1 = {'aeiou'} # sem uso do construtor
print(type(vogais_1), vogais_1)

#O construtor interpreta como um iterável e cria um conjunto em que cada caractere 
#é um elemento, eliminando valores duplicados.
vogais_2 = set('aeiouaaaaaa') # construtor com string
print(type(vogais_2), vogais_2)

vogais_3 = set(['a', 'e', 'i', 'o', 'u']) # construtor com lista
print(type(vogais_3), vogais_3)

vogais_4 = set(('a', 'e', 'i', 'o', 'u')) # construtor com tupla
print(type(vogais_4), vogais_4)

print(set('banana'))
