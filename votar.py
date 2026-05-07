'''
🔹 5. Pode votar?
Peça a idade e informe:
• Pode votar (idade >= 16)
'''
idade :int = int(input("Qual sua idade: "))

if idade >= 16:
    print("Você já pode votar,Parabéns!")
elif idade< 16:
    print("Ainda não é sua vez de votar")
else:
    print("Não deixe a idade vazia :(")