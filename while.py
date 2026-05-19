'''
1- Faça um programa ,utilizando while ,que mostre na tela os numero de 0  a 100.
2- Faça um programa ,utilizando while ,que mostre na tela os numero de 0  a N em que N é definido pelo usuario
3- Faça um programa ,utilizando while ,que mostre na tela  todos os numero pares de 0  a 100.
4-Desenvolva um programa que exibe a  tabuada do número 5
'''


'''1
cont= 0 
while cont <=100:
    cont = cont + 1
    print(f"Estamos no {cont}")
    '''
'''2
cont= 0 
N:int = int(input("Digite o valor de N: "))

while cont <=N:
    cont = cont + 1
    print(f"Estamos no {cont}")'''
    

'''3
valores par 
cont= 0

while cont <=100:
    cont = cont + 2
    print(f"{cont}")
'''

'''For 4'''

numero= 5

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    