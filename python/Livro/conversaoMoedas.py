#Para esse cálculo existem parâmetros que são obrigatórios e outros opcionais,
#portanto a função deve ser capaz de lidar com esse tipo de dinâmica

def calcular_valor(valor_prod, qtde, moeda="real", desconto=None, acrescimo=None):
    v_bruto = valor_prod * qtde
    
    if desconto:
        v_liquido = v_bruto - (v_bruto * (desconto / 100))
    elif acrescimo:
        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
    else:
        v_liquido = v_bruto
    
    if moeda == 'real':
        return v_liquido
    elif moeda == 'dolar':
        return v_liquido * 5
    elif moeda == 'euro':
        return v_liquido * 5.7
    else:
        print("Moeda não cadastrada!")
        return 0

valor_total_sem_desconto = calcular_valor(valor_prod=50, qtde=25)
valor_a_pagar = calcular_valor(valor_prod=50, qtde=25, desconto=10)
valor_do_desconto = valor_total_sem_desconto - valor_a_pagar


print(f"O valor total da compra R$: {valor_total_sem_desconto}"
      f"\no valor desconto foi R$: {valor_do_desconto}"
      f"\no valor final da conta é R$: {valor_a_pagar}")
