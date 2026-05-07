'''Peça um número  e informe se ele é 

*Positivo
*Negativo
*zero  
teste lógico com if
'''

numero :int =int(input("informe o número: "))

if numero > 0:
   print(f"Numero digitado é {numero} positivo")
elif numero < 0:
   print(f"Numero digitado é {numero} negativo")
else:
    if numero == 0:
         print(f"Numero digitado é {numero}  ")
    else:
        print(f"{numero} Negativo")
print("Pressione enter para sair")