'''
14 Distância até 200km: R$ 0,50/km. Acima de 200km: R$ 0,45/km. Se for feriado
(sim/nao), aplique uma taxa extra de 10% sobre o valor final.
'''

distancia:float =float(input("Informe a Distância: "))
feriado = input("É feriado (sim| nao):")


if distancia <=200:
    valor =distancia *0.50
else:
    valor =distancia *0.45
    
if  feriado =="sim":
    valor =valor *1.10
print(f" o valor final é  R${valor:.2f}")