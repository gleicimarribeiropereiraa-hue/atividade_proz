'''
🔹 7. Número dentro do intervalo
Peça um número e verifique se ele está entre 0 e 100.

'''

numero :int =int(input("Digite o número:  "))

if numero == 0 | numero <= 100:
    print(f"O número digitado {numero} está entre 0 e 100")
elif numero < 0 | numero >= 100:
   print(f"O número digitado {numero}  não está entre 0 e 100")
else:
    print("Operação Inválida número não pode ficar em branco")
