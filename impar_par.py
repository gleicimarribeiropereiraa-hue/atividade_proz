'''
2 - Faça um algoritmo para receber um número qualquer 
e imprimir na tela se o número é par ou ímpar, positivo ou negativo.
'''
numero : int =int(input("Digite valor: "))


if numero > 0  and numero % 2 ==0:
    print(f"{numero} é par e positivo")
elif numero > 0  and numero % 2 !=0:
    print(f"{numero} é impar")
else :
    print(f"{numero} é  negativo")
    
    