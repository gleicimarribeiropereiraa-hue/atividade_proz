'''Peça doi números e mostre qual é o maior'''

num1:int=int(input("Digite o número: "))
num2:int=int(input("Digite o número: "))


if num1 > num2:
    print(f"O numero digitado {num1} é maior ")
elif num1 ==num2:
    print(f"Números {num1} e {num2} são iguais")
else:
    print(f"Numero digitado {num2} é maior")

