'''
7 Peça o peso (kg) e a altura (m). Calcule o IMC (peso / altura2). Exiba: "Abaixo do
peso" (IMC < 18.5), "Peso normal" (18.5 a 24.9) ou "Sobrepeso" (≥ 25).

'''
peso:float =float(input("Informe seu peso: "))
altura:float =float(input("Informe sua altura: "))

imc= peso / (altura **2)

if imc <18.5:
    print(f"Abaixo do Peso seu IMC é : {imc:.2f}" )
elif imc >18.5 and imc <= 24.9:
    print(f"Peso Normal seu IMC é :{imc:.2f}")
else :
    print(f"Sobrepeso seu IMC é :{imc:.2f}")
