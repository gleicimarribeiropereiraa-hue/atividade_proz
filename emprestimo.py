'''
11 Peça o valor do imóvel, o salário e o prazo (anos). A prestação mensal não pode
exceder 30% do salário. Regra Especial: Se o comprador tiver > 60 anos, o limite
sobe para 35%.
'''
valor_imovel :float =float(input("Informe valor do imóvel: "))
salario :float =float(input("Informe seu salario: "))
prazo :int =int(input("Informe prazo para pagar em anos: "))
idade :int =int(input("Informe sua idade: "))

meses = prazo * 12
prestacao =valor_imovel / meses
#Regra Especial: Se o comprador tiver > 60 anos
if idade > 60:
    limite = salario * 0.35
else:
    limite = salario * 0.30

if prestacao <= limite:
    print("Financiamento aprovado")
    print(f" o valor da prestação é {prestacao:.2f}")
else:
    print("Não está elgível ao financiamento")
    print(f" o valor da prestação é {prestacao:.2f}")
    print(f"Limite permitido é {limite:.2f}")
