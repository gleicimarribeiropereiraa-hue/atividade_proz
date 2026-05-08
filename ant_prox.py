'''
4 - Faça um algoritmo que receba um número inteiro e
imprima na tela o seu antecessor e o seu sucessor.
'''
numero :int = int(input("Digite número: "))

print(f"Numero digitado foi {numero}")

if numero != "":
    print(f"o anterior é {numero -1}")
    print(f"O sucessor é {numero +1}")

else:

    print("Você precisa digitar um número")