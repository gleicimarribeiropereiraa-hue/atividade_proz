numero :int =int(input("Digite número: "))

print(f"Numero digitado foi {numero}")

if numero != "":
    print(f"o anterior é {numero -7}")
    print(f"O sucessor é {numero +7}")

else:
    print("Você precisa digitar um número")