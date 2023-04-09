#Em uma estrutura de repetição sempre haverá uma estrutura decisão, 
#pois a repetição de um trecho de código sempre está associada a uma condição. 
#Ou seja, um bloco de comandos será executado repetidas vezes, até que
#uma condição não seja mais satisfeita.

#O comando while deve ser utilizado para construir e controlar a 
#estrutura decisão, sempre que o número de repetições não seja conhecido. 

#Por exemplo, quando queremos solicitar e testar se o número digitado pelo usuário
#é par ou ímpar. Quando ele digitar zero, o programa se encerra. 

#Livro - página 27
numero = 1

while numero != 0:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Número par!\n")
    else:
        print("Número ímpar!\n")
