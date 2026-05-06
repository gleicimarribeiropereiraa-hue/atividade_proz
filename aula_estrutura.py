'''
Uma loja aplica desconto de 12% em compras acima de 300R$ 
crie um programa que exiba o valor de desconto e o preço final'''


valor_produto :float = 12.50
quantidade_compra: int =int (input("Digite a quantidade de compra: "))

total :float =valor_produto*quantidade_compra

if total >= 300:
    desconto: float = total*0.12
    total_desconto:float =total - desconto
    print(f"o valor da compra foi R${total}")
    print(f"o valor do desconto foi R${desconto}")
    print(f"O valor final é R${total_desconto}")
else:
    print(f"O valor comprado foi:  {total}")

print("informe nome do comprador: ")
nome:str =input("digite nome do Comprador:")
print(f"Nota Fiscal {nome}")