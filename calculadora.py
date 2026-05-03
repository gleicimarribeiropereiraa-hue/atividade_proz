#Definir numeros
#Os números podem ser alterados


num1 :int = 10
num2:int = 20


soma: int =num1 + num2
subtracao: int = num1 - num2
divisao :float = num1 / num2
multiplicacao :int = num1 * num2


print (f'Numero 1: {num1}')
print (f'Numero 2: {num2}')

print('-' * 15)
print(f"A soma é: ", soma)
print(f"A subtração é: ", subtracao)
print(f"A divisão é: ", divisao)
print(f"A multiplicação é: ", multiplicacao)


num1  = int(input("Digite o primeiro número: "))
num2  = int(input("Digite o segundo número: "))

sinal  = input("Digite a operação desejada (+, -, *, /): ")

if sinal == '+':
    resultado :int = num1 + num2
elif sinal == '-':
    resultado :int = num1 - num2
elif sinal == '*':
    resultado :int = num1 * num2
elif sinal == '/':
    if num2 != 0:
        resultado :int = num1 / num2
    else:
        resultado :int = "Erro: Não existe Divisão por zero"
else:
    resultado = "Operação inválida"
print("O resultado é: ", resultado)


