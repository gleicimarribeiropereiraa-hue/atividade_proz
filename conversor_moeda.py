'''
2 Peça um valor em Reais (float) e a cotação atual do Dólar. Calcule e exiba o valor
convertido para Dólares.
'''
valor_real :float =float(input("Informe valor:" ))
cotacao_dolar:float =float(input("Informe cotação atual dólar: "))

valor_dolar:float = valor_real / cotacao_dolar

print(f" O valor em dólar é: US$  {valor_dolar:.2f}")