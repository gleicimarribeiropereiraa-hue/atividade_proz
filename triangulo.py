'''
10 Peça três lados. Verifique se formam um triângulo (a soma de dois lados deve
ser maior que o terceiro). Se sim, classifique em: Equilátero (3 iguais), Isósceles
(2 iguais) ou Escaleno (todos diferentes).
'''
a: int = int(input("Informe valor do lado 1: "))
b: int = int(input("Informe valor do lado 2: "))
c: int = int(input("Informe valor do lado 3: "))



if a + b > c and a + c > b and b + c > a:
    print(f"Foma um triangulo com os lados {a}, {b}, {c}")
    
    if a ==b !=c:
        print(f"lados iguais {a} e {b} é Isósceles")
    elif a == b ==c :
        print(f"lados iguais {a} , {b} e {c} é Equilátero")
    else:
        print(f"todos os lados diferentes {a} , {b} , {c} é Escaleno")