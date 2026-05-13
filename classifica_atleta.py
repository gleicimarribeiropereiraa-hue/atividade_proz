'''
5 Receba a idade de um nadador e exiba sua categoria:
- Menor que 5 anos: "Muito jovem" 
- 5 a 7 anos: "Infantil A"
- 8 a 10 anos: "Infantil B"
- 11 a 17 anos: "Juvenil"
- 18 ou mais: "Sênior"
'''
idade:int = int(input("Informe Idade do Nadador: "))

if idade<= 5:
    print("Muito jovem")
elif idade > 5 and idade <=7:
    print("Infantil A")
elif  idade > 8 and idade <=10:
    print("Infantil B")
elif  idade >=11 and idade <=17:
    print("Juvenil")
else:
    print("Sênior")