'''
🔹 8. Desconto simples
Peça o valor de um produto:
• Se for maior que 100 → aplicar 10% de desconto
• Senão → sem desconto
Mostre o valor final.
'''
valor:int = int(input("Digite valor do produto: "))
quantidade : int = (input("Digite quantidade do produto : "))
desconto =0
valor_desc=0

if valor > 100:
    print("O valor tem desconto de 10%")
elif valor < 100:
    print("O valor não tem desconto ")
else:
    print("O valor não pode ficar zerado")   
