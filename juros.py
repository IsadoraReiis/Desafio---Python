valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

#TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

def calcular_valor_final(capital_inicial, taxa_juros, anos):
    montante = capital_inicial * (1 + taxa_juros) ** anos
    return montante

valor_final = calcular_valor_final(valor_inicial, taxa_juros, periodo)
print("Valor final do investimento: R$ {:.2f}".format(valor_final))