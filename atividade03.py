numero = int(input("Digite o numero para saber se é par ou ímpar: "))

p = numero % 2 == 0

if p:
    print("Este número é par")
else: 
    print("Este número é ímpar")