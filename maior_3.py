'''
🔹 9. Maior de três números
Peça três números e mostre o maior deles.
👉 (sem usar estrutura avançada — só se)
'''

num1 : int = int(input("Informe Número 1: "))

num2 : int = int(input("Informe Número 2: "))

num3 : int = int(input("Informe Número 3: "))

if num1 > num2 & num3:
    print(f"Numero {num1} é maior que {num2} e {num3}")
elif num2 > num1 & num3:
    print(f"Numero {num2} é maior que {num1} e {num3}")
elif num3 > num1 & num2:
    print(f"Numero {num2} é maior que {num1} e {num3}")
else:
    print("Operação inválida informe o número")