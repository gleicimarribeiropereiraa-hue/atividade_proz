'''
4 Peça duas notas, calcule a média aritmética e exiba "Aprovado" se a média for
maior ou igual a 7.0, e "Reprovado" caso contrário.
'''
nota_1: float = float(input("Digite a primeira nota: "))
nota_2: float = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2) / 2

if media>=7:
    print(f"Sua media foi {media},você está aprovado")
else:
    print(f"Você não atingiu a media para passar tirou {media}, Reprovado")