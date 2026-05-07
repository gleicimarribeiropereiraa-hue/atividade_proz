'''
Peça dois números e diga se eles são:
• Iguais
• Diferentes
'''

numero_1 :int =int(input("Digite o número: "))
numero_2 :int =int(input("Digite o número: "))

if numero_1 == numero_2:
    print(f"Os números {numero_1} e {numero_2} são iguais ")
elif numero_1 != numero_2 :
    print(f"Os números {numero_1} e {numero_2} são diferentes ")
else:
    print("Você não informou nenhum número")
    