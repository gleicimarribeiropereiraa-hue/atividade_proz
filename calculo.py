'''
3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, 
deverá somar os dois valores, caso contrário devera multiplicar A por B. Ao final de qualquer 
um dos cálculos deve-se atribuir o resultado a uma variável C e imprimir seu valor na tela.
'''
a :int = int(input("Digite numero:"))
b :int = int(input("Digite numero:"))



if a == b:
   c = a + b
   print(f"O resultado é {c}")
else:
     c = a * b
     print(f"O resultado é {c}")  
