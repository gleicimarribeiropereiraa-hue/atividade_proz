''''
6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

'''

numero :float = float(input("Digite número: "))

aliquota :float = 0.05

soma:float =  numero + (numero * aliquota)

print(f"valor reajustado {soma}")