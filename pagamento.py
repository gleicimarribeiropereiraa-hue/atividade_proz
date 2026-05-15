''''
15 Peça o valor total. Opções: À Vista (10% desconto), Cartão Débito (5% desconto)
ou Cartão Crédito (preço normal). Use condicionais aninhadas.
'''

valor_total :float=float(input("Informe valor total: "))
forma = input("Qual é a forma de pagamento a_vista |debito |credito: ")

if forma =="a_vista":
    valor_final = valor_total * 0.90 #10% de desconto
elif forma =="debito":
    valor_final = valor_total * 0.95
elif forma =="credito":
    valor_final =valor_total  #sem desconto
else:
   print("Forma de pagamento inválida")
   valor_final = None

if valor_final is not None:
    print(f"Valor final: R$ {valor_final:.2f}")
