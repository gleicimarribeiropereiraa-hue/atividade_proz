'''
3 Peça um número inteiro ao utilizador. Use a estrutura if/else para informar se
o número digitado é Par ou Ímpar.
'''
numero : int =int(input("Digite valor: "))


if numero > 0 and numero % 2 ==0:
    print(f"{numero} é par ")

else :
    print(f"{numero} é impar")