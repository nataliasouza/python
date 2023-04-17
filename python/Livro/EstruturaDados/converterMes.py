#Vamos implementar uma função que recebe uma data no formato dd/mm/aaaa e converte o mês
#para extenso. Então, ao se receber a data 10/05/2020, a função deverá 
#retornar: 10 de maio de 2020. 

def converter_mes_para_extenso(data):
    meses = '''janeiro fevereiro março
      abril maio junho julho agosto
      setembro outubro novembro
      dezembro'''.split()
    dia, mes, ano = data.split('/')
    mes_extenso = meses[int(mes) - 1] # O mês 1, estará na posição 0!
    return f'{dia} de {mes_extenso} de {ano}'

print(converter_mes_para_extenso('01/12/1984'))