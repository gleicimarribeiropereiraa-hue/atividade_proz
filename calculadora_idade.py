'''
1 Escreva um programa que peça o nome e a idade do utilizador. Converta a idade
para um número inteiro e exiba uma mensagem: "Olá [Nome], você já viveu
aproximadamente [Idade * 12] meses".
'''
nome :str = input("Qual seu nome: ")
idade :int = int( input("Qual sua idade: "))

meses = idade * 12

print(f"Olá {nome},você já viveu {meses} meses")
