#Um arquivo JSON é composto por elementos na forma chave-valor.
#Criar uma função que, com base nas informações que lhe serão fornecidas,
#retorne uma lista com os e-mails que ainda precisam ser enviados.

#Exercício

#Para esse projeto, você e mais um desenvolvedor foram alocados. Enquanto seu 
#colega trabalha na extração dos dados da API, você cria a lógica para gerar a função.
#Foi combinado, entre vocês, que o programa receberá dois dicionários referentes aos dois
#arquivos que foram gerados. O dicionário terá a seguinte estrutura: 
#três chaves (nome, email, enviado), cada uma das quais recebe uma lista de informações;
#ou seja, as chaves nome e email estarão, respectivamente, associadas a uma lista de nomes
#e uma de emails. por sua vez, a chave enviado estará associada a uma lista de valores 
#booleanos (True-False) que indicará se o e-mail já foi ou não enviado.

def extrair_lista_email(dict_1, dict_2):    
    lista_1 = list(zip(dict_1['nome'], dict_1['email'], dict_1['enviado']))
    #imprimimos uma única tupla construída para que pudéssemos checar a construção.
    print(f"Amostra da lista 1 = {lista_1[2]}")

    #função zip() conseguimos extrair cada registro do dicionário,
    #passando com parâmetro a lista de nomes, de e-mails e o status do enviado, 
    #e transformamos seu resultado em uma lista
    lista_2 = list(zip(dict_2['nome'], dict_2['email'], dict_2['enviado']))

    #Colocados todos os dados das duas listas em uma só. 
    dados = lista_1 + lista_2

    #dados agora possui todos os dados das duas listas e vai mostrar o conteúdo
    #da posição 0 e 1 [:2], a segunda posição não é incluída.    
    print(f"\nAmostra dos dados = \n{dados[:2]}\n\n")
        
    # Selecionamos o item[1], estamos pegando o valor que ocupa a posição 1 da tupla, o e-mail.
    #iterando sobre todos os dados, teremos uma lista com todos os e-mails
    #Queremos uma lista com o email de quem ainda não recebeu o aviso.
    # Para fazer esse filtro, incluímos na listcomp uma estrutura condicional (if) que 
    #adiciona somente "if not item[2]", ou seja, somente se o item[2] não tiver valor True.  
    emails = [item[1] for item in dados if not item[2]]
    
    return emails

dados_1 = {
    'nome': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker', 'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
    'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org', 'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu', 'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com', 'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
    'enviado': [False, False, False, False, False, False, False, True, False, False]
}

dados_2 = {
    'nome': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis', 'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
    'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com', 'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net', 'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
    'enviado': [False, False, False, True, True, True, False, True, True, False]
}

emails = extrair_lista_email(dict_1=dados_1, dict_2=dados_2)
print(f"E-mails a serem enviados = \n {emails}")

