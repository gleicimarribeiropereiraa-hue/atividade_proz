'''
13 Determine se um ano é bissexto. Regra: Divisível por 4 E (Não divisível por 100
OU divisível por 400).

'''

ano:int =int(input("Informe o Ano :"))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")
