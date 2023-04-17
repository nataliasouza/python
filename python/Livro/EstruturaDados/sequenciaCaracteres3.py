#sobre a função split(), usada para "cortar" um texto e transformá-lo em uma lista.
#Essa função pode ser usada sem nenhum parâmetro: texto.split().
#Nesse caso, a string será cortada a cada espaço em branco que for encontrado

texto = "Aprendendo Python na disciplina de linguagem de programação."
print(f"texto = {texto}")
print(f"Tamanho do texto = {len(texto)}\n")

palavras = texto.split()#corta o texto em cada espaço em branco.
print(f"palavras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}")