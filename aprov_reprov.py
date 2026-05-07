'''
🔹 4. Aprovado ou reprovado
Peça a nota do aluno e informe:
• Aprovado (nota >= 6)
• Reprovado
'''
nota :float =float(input("Informe nota: "))

if nota >= 6:
    print("Parabéns você foi aprovado!")
elif nota < 6:
    print("Infelizmente você foi  reprovado!")
else:
    print("Nota não pode ficar vazia!")