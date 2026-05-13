'''
8 Aplique aumentos baseados no salário atual:
- Até R$ 1.500,00: +20%
- R$ 1.500,01 a R$ 3.000,00: +15%
- Acima de R$ 3.000,00: +10%
Exiba o salário antigo, o percentual e o novo valor.
'''
salario :float = float(input("Informe seu salário: "))

if salario ==1500.00:
    percentual =20
elif salario <=3000.00:
    percentual =15
else:
    percentual=10
 
aumento = salario * (percentual / 100 )
novo_salario = salario + aumento

print(f"Salário antigo: R$ {salario:.2f}")
print(f"Percentual de aumento: {percentual}%")
print(f"Novo salário: R$ {novo_salario:.2f}")