'''
8) Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores. 

'''

total_eleitores: int =int(input("Quantos eleitores  na cidade ?"))
votos_brancos:int =int(input("Quantos votaram em branco? "))
votos_nulos:int =int(input("Quantos votos nulo? "))
votos_validos:int =int(input("Quantos votos validos? "))


percentual_branco :int =int(votos_brancos /total_eleitores) *100
percentual_nulo :int =int(votos_nulos /total_eleitores)*100
percentual_validos :int =int(votos_validos /total_eleitores)*100


print(f"O valor percentual é: {percentual_branco}")
print(f"O valor percentual é: {percentual_nulo}")
print(f"O valor percentual é: {percentual_validos}")




