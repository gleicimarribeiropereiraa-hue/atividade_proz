operacao:str =input("Digite A:Sacar -B:Depositar -C:Encerrar: ")
saldo:float = 1000

match(operacao):
    case "A":
        valor:float =float(input("Digite o valor do Saque: "))
        saldo = saldo - valor
        print(f"Seu saldo  atual é  {saldo}")
    case "B":
        valor:float =float(input("Digite o valor do Depósito: "))
        saldo = saldo + valor
        print(f"Seu saldo  atual é  {saldo}")
        
    case "C":
        valor:float =float(input("Digite o valor do Saque: "))
        saldo = saldo - valor
        print(f"Seu saldo  atual é  {saldo}")
    case "_":
        print(f"Opção Inválida")