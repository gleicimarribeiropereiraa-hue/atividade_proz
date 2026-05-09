'''
Um aluno pod está aprovado se nota > 6
recuperação se nota  < 6  e maior que 4
reprovado se nota < 4
se nota == 0
'''
nota :int= int(input("Informe a nota :"))
if nota == 0:
    print("inativo")
elif nota >= 6:
    print("aprovado")
elif  nota < 4:
    print("Reprovado")
else:
    print("Recuperação")
