''''
🔹 6. Número maior que 10
Peça um número e diga:
• Maior que 10
• Menor ou igual a 10
'''

num :int = int(input("Informe um número: "))

if num > 10:
    print(f"Numero {num} é maior que 10")
elif num <= 10:
   print(f"Numero {num} é menor ou igual a 10")
else:
   print(f"Numero {num} não pode ficar vazio")

