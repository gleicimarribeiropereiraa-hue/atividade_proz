'''
1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima
na tela a soma entre A e B e mostre se a soma é menor que C.

'''

a :int =int(input("Digite valor: "))

b :int =int(input("Digite valor: "))


c :int =int(input("Digite valor: "))

soma:int = a + b

if soma <= c :
    print(f"O valor da soma {soma} é menor que {c}")
    
else:
    print(f"{soma} é maior que {c}")