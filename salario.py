'''
5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário 
de um usuário, calcule quantos salários mínimos esse usuário ganha e imprima na tela
o resultado. (Base para o Salário mínimo R$ 1.608,20).
'''
salario_minimo :float = 1608.20

salario_usuario: float = float(input("Digite seu salrio: "))

quantidade = salario_usuario / salario_minimo


print(f"Você ganha apenas {quantidade:.2f} salários")

