'''
12 Peça a temperatura e se está chovendo (sim/nao).
- Frio (< 15) e Chuva: "Casaco impermeável e bota"
- Frio (< 15) e Sem Chuva: "Casaco pesado"
- Calor (≥ 15) ou Sem Chuva: "Roupas leves"
'''
temperatura :int =int(input("Informe a temperatura: "))
chuva = input("Está chovendo  (sim | nao): ")

if temperatura < 15 and chuva =="sim":
    print ("Frio e chuvoso: Casaco impermeável e bota")
elif temperatura < 15 and chuva =="nao":
    print ("Frio: Casaco pesado")
else:
    print (" Calor: Roupas leves")
