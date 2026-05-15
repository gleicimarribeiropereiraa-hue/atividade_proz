'''
9 Aprovação requer: Média ≥ 7.0 E Presença ≥ 75%. Peça as notas e a frequência.
Se reprovado, informe se foi por nota, por falta ou por ambos.
'''

nota :int=int(input("Digite nota aluno: "))
presenca :int=int(input("Digite presenca aluno: "))

if nota >=7 and presenca>= 75:
    print(f'Parabeéns vocâ tingiu {nota} e {presenca},está aprovado')
elif nota >= 7 and presenca >= 0:
    print(f"Você tem nota:{nota},mas sem presença,está reprovado")
elif nota >=7 and presenca >= 0:
    print(f"Você tem presença:{presenca},mas sem nota,está reprovado")
elif nota >= 0 and presenca >= 0:
    print(f"Você reprovou por nota:{nota} e presença:{presenca}")
else:
    print(f"Não pode ficar vazio,tente novamente")